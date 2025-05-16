import tkinter as tk
from tkinter import Label, Frame, Entry, Button

def calcular_imc():
    try:
        pesoValor = float(peso.get())
    except ValueError:
        resultado['text'] = 'peso inválido'
        return
    try:
        alturaValor = float(altura.get())
    except ValueError:
        resultado['text'] = 'altura inválida'
        return
    IMC = pesoValor / (alturaValor ** 2)
    resultado['text'] = f'Seu IMC é de {IMC:.2f}'


janela = tk.Tk() 

tk.Label(janela, text='Para saber seu IMC digite os valores abaixo',pady=40).grid(column=1,row=1, columnspan= 2)
frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1)

Label(frame, text= 'Qual o seu peso?').grid(column=1, row=2)
Label(frame, text= 'Qual a sua altura?').grid(column=1, row=3)

peso = Entry(frame)   
peso.grid(column=2, row = 2)

altura = Entry(frame)
altura.grid(column=2,row = 3)

Button(frame, text='Calcular', command= calcular_imc).grid(column=2, row = 4)

resultado = Label(frame)
resultado.grid(column=1, row = 5, columnspan=2)

janela.title('Calculadora de IMC')
janela.mainloop()
