import math  # funçoes matematicas
from tkinter.ttk import *
from tkinter import *  # interface grafica
import matplotlib.pyplot as plt  # contruçao do grafico
import seaborn as sns  # estilos para o grafico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # faz o grafico ser uma figura

# cria a interface
homePage = Tk()
homePage.title("EQUAÇÃO CALCULO 1")
homePage.geometry("500x320")


# cria o grafico
def grafico (X, Y):
    window = Tk()
    window.title("EQUAÇÃO:  x³+5sen(x)=−2x−4")

    sns.set_style('whitegrid')
    figura = plt.Figure(figsize=(18, 9), dpi=75, facecolor='#4dffdb')
    figura.add_subplot(111).scatter(X, Y)

    canvas = FigureCanvasTkAgg(figura, window)
    canvas.get_tk_widget().grid(row=1, column=1)

    window.mainloop()


# calculo da equaçao
def funcao (n):
    resultado = round(((n * n * n) + (5 * (math.sin(n))) + (2 * n) + 4), 5)
    return resultado


# esta parte analiza se o resultado x no intervalo possui solucao, e faz se aproximar no meio da funçao
def interpretacao (entradaMaior, entradaMenor):
    calcX = []
    valorMenor = round(entradaMenor, 5)
    valorMaior = round(entradaMaior, 5)
    # armazena em uma lista os resultados se aproximando do meio
    while (valorMenor - valorMaior <= 0.12):
        for i in range(1):
            valorMenor += 0.01
            calcX.append(valorMenor)
            for ii in range(1):
                valorMaior -= 0.01
                calcX.append(valorMaior)

    janelaResultados = Tk()
    janelaResultados.title("RESULTADOS DA FUNÇÃO")
    janelaResultados.geometry("350x500")

    scrollbar = Scrollbar(janelaResultados, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    textoSaida = Text(janelaResultados, wrap="none", yscrollcommand=scrollbar.set,font=("Arial", 14))

    # aplica os resultados na equação em ordem cronologica
    resultados = []
    positionX = []
    posicao = -1
    valorMenor0 = False
    valorMaior0 = False
    pares=0
    for i in range(len(calcX)):
        posicao += 1
        x = calcX[posicao]


        # o try e o except servem para ver se há um valor que cause a descontinuidade da função
        try:
            saidaCalculo = funcao(x)
            if saidaCalculo <= 0 and valorMenor0 == False:
                valorMenor0 = True
            if saidaCalculo >= 0 and valorMaior0 == False:
                valorMaior0 = True
            resultados.append(saidaCalculo)
            positionX.append(x)

            escreveSaida = str(f"F({x:.2f}) = {saidaCalculo}\n")

            textoSaida.insert("end",escreveSaida)
            textoSaida.pack(side="top", fill="y")

            pares+=1
            if pares==2:
                pares=0
                textoSaida.insert("end", "\n")

            intervalo = True
        # caso ele encontre um limite aparecerá a mensagem contida na linha 74 e 82
        except ZeroDivisionError or ValueError or (x == entradaMenor and len(resultados) == 1):
            janelaResultados.destroy()
            intervalo = False
            print("\nNão é possível afirmar que existe solução neste intervalo, tente outros dois números.\n")
            alertError = Tk()
            alertError.title("!")

            def errorSaida ():
                alertError.destroy()
                entradas()

            content = Label(alertError,
                            text="Não é possível afirmar que existe solução neste intervalo, tente outros dois números.")
            content.config(font=("Arial", 14))
            content.grid(column=2, row=2)

            voltar = Button(alertError, text="Retornar", command=errorSaida, padx=40, pady=25)
            voltar.grid(column=2, row=3)
            voltar.config(font=("Arial", 14))

            alertError.mainloop()
            break

    # esta parte analisa os dados encontrados no intervalo e gera uma resposta de saida
    if intervalo == True:
        respostaSaida = str("")
        if valorMaior0 == True and valorMenor0 == True:
            respostaSaida = f"No intervalo de [{round(entradaMenor, 5)},{round(entradaMaior, 5)}] existe um ponto c, e que no gráfico da função existe um ponto f(x)=0."
        else:
            respostaSaida = f"No intervalo de [{round(entradaMenor, 5)},{round(entradaMaior, 5)}] existe um ponto c."
        print(respostaSaida)

        saidaResultado = Tk()
        saidaResultado.title("TEOREMA DO VALOR INTERMEDIÁRIO")

        textoResposta = Label(saidaResultado, text=respostaSaida)
        textoResposta.config(font=("Arial", 14))
        textoResposta.grid(column=1, row=1, columnspan=3, padx="20", pady="20")

        abrirGrafico = Button(saidaResultado, text="Ver gráfico", padx=40, pady=25,
                              command=lambda: grafico(positionX, resultados))
        abrirGrafico.grid(padx="10", pady="10", column=1, row=2, columnspan=3)
        abrirGrafico.config(font=("Arial", 14))

        saidaResultado.mainloop()


    scrollbar.config(command=textoSaida.yview)
    janelaResultados.mainloop()
# esta parte cria as entradas da funçao e ás ordena de maneira crescente
def entradas ():
    def pushDatas ():
        valor1list = list(entrada1.get())

        for count in range(len(valor1list)):  # codigo para aceitar "," e ".". Ex: 5,5 == 5.5
            if valor1list[count] == ",":
                valor1list[count] = "."
        valor1float = float("".join(valor1list))

        valor2list = list(entrada2.get())
        for count in range(len(valor2list)):
            if valor2list[count] == ",":
                valor2list[count] = "."
        valor2float = float("".join(valor2list))

        # ordena-os de maneira crescente
        if valor1float != "" and valor2float != "" and (valor1float!=valor2float):
            if valor1float > valor2float:
                interpretacao(valor1float, valor2float)
            else:
                interpretacao(valor2float, valor1float)

    Label(homePage, text="Insira os valores [A,B] para calculo do intervalo:", font=("Arial", 16)).grid(column=1, row=0,columnspan=3,padx="10",pady="10")
    Label(homePage, text="f(x)=x³+5sen(x)+2x+4", font=("Arial", 16)).grid(column=1, row=1, columnspan=3, padx="10",
                                                                          pady="10")

    Label(homePage, text="A:", font=("Arial", 16), ).grid(column=1, row=2, padx="10", pady="10")

    entrada1 = Entry(homePage, width=25)
    entrada1.config(font=("Arial", 14))
    entrada1.grid(column=2, row=2, padx="10", pady="10")

    Label(homePage, text="B:", font=("Arial", 16)).grid(column=1, row=3, padx="10", pady="10")

    entrada2 = Entry(homePage, width=25)
    entrada2.grid(column=2, row=3, padx="10", pady="10")
    entrada2.config(font=("Arial", 14))

    calcular = Button(homePage, text="Calcular", command=pushDatas, padx=40, pady=25)
    calcular.grid(padx="10", pady="10", column=1, row=4, columnspan=3)
    calcular.config(font=("Arial", 14))


# o codigo inicia aqui(chamando a funçao que irá pedir os valores e ordenalos)
entradas()
homePage.mainloop()
