import tkinter as tk
from tkinter import Label, Frame, Entry, Button

def calculaImc():
    try:
        IMC = float(peso.get())/float(altura.get()) ** 2

        resultado['text'] = f'Seu IMC é de {IMC:.2f}'
    except ValueError:
        resultado['text'] = f'Os valores estao errados'

janela = tk.Tk() 

tk.Label(janela, text='Para saber seu IMC digite os valores abaixo',pady=40).grid(column=1,row=1, columnspan= 2)
frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1)

Label(frame, text= 'Qual o seu peso?').grid(column=1, row=2)
Label(frame, text= 'Qual a sua altura?').grid(column=1, row=3)

peso = Entry(frame)   
peso.grid(column=2, row = 2)

altura = Entry(frame)
altura.grid(column=2,row = 3)

Button(frame, text='Calcular', command= calculaImc).grid(column=2, row = 4)

resultado = Label(frame)
resultado.grid(column=1, row = 5, columnspan=2)

janela.title('Caladora de IMC')
janela.mainloop()
