import math #funçoes matematicas
from tkinter.ttk import *
from tkinter import * #interface grafica
import matplotlib.pyplot as plt #contruçao do grafico
import seaborn as sns #estilos para o grafico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #faz o grafico ser uma figura


homePage=Tk()
homePage.title("EQUAÇÃO CALCULO 1")
homePage.geometry("500x320")

def grafico(X,Y):
    window=Tk()
    window.title("EQUAÇÃO:  x³+5sen(x)=−2x−4")

    sns.set_style('whitegrid')
    figura = plt.Figure(figsize=(18,9), dpi=75,facecolor='#4dffdb')
    figura.add_subplot(111).scatter(X,Y)


    canvas = FigureCanvasTkAgg(figura, window)
    canvas.get_tk_widget().grid(row=1,column=1)


    window.mainloop()

#função
def calculoFunctionI(x,entradaMenor):
    resultados = []
    positionX = []
    while entradaMenor<=x:
        result=round(((x*x*x)+(5*(math.sin(x)))+(2*x)+4),5)
        if result!=ZeroDivisionError or result!=ValueError or (x==entradaMenor and len(resultados)==1):
            resultados.append(result)
            positionX.append(x)
            print(f"{x:.2f} = {result}")
            x-=0.1
            intervalo = True
        else:
            intervalo=False
            print("\nNão é possível afirmar que existe solução neste intervalo, tente outros dois números.\n")
            homePage.destroy()
            alertError=Tk()
            alertError.title("!")
            def errorSaida():
                alertError.destroy()
                entradas()

            content = Label(alertError,text="Não é possível afirmar que existe solução neste intervalo, tente outros dois números.")
            content.config(font=("Arial", 14))
            content.grid(column=2, row=2)

            voltar = Button(alertError, text="Retornar", command=errorSaida, padx=40, pady=25)
            voltar.grid(column=2, row=3)
            voltar.config(font=("Arial", 14))

            alertError.mainloop()
            break
    if intervalo==True:
        grafico(positionX,resultados)

def entradas():
    def pushDatas():
        valor1list = list(entrada1.get())
        for count in range(len(valor1list)):
            if valor1list[count]==",":
                valor1list[count]="."
        valor1float=float("".join(valor1list))

        valor2list = list(entrada2.get())
        for count in range(len(valor2list)):
            if valor2list[count] == ",":
                valor2list[count] = "."
        valor2float = float("".join(valor2list))
        if valor1float!="" and valor2float!="":
            if valor1float>valor2float:
                calculoFunctionI(valor1float,valor2float)
            else:
                calculoFunctionI(valor2float,valor1float)

    Label(homePage, text="Insira os valores [A,B] para calculo do intervalo:", font=("Arial", 16)).grid(column=1,row=0,columnspan=3, padx= "10", pady="10")
    Label(homePage, text="f(x)=x³+5sen(x)+2x+4", font=("Arial", 16)).grid(column=1, row=1,columnspan=3,padx="10",pady="10")

    Label(homePage, text="A:", font=("Arial", 16),).grid( column=1,row=2,padx= "10", pady="10")

    entrada1 = Entry(homePage, width=25)
    entrada1.config(font=("Arial", 14))
    entrada1.grid(column=2,row=2, padx= "10", pady="10")

    Label(homePage, text="B:", font=("Arial", 16)).grid(column=1,row=3, padx= "10", pady="10")

    entrada2 = Entry(homePage, width=25)
    entrada2.grid(column=2,row=3, padx= "10", pady="10")
    entrada2.config(font=("Arial", 14))


    calcular = Button(homePage,text="Calcular",command=pushDatas,padx=40, pady=25)
    calcular.grid(padx= "10", pady="10", column=1,row=4,columnspan=3)
    calcular.config(font=("Arial", 14))

entradas()


homePage.mainloop()
