import tkinter as tk
from tkinter import LabelFrame, Button, Label, PhotoImage
import random

def escolheuPedra():
    jokenpo(escolhaUsuario='Pedra')

def escolheuPapel():
    jokenpo(escolhaUsuario='Papel')

def escolheuTesoura():
    jokenpo(escolhaUsuario='Tesoura')


def jokenpo(escolhaUsuario):
    escolhaComputador = random.choice(['Pedra','Papel','Tesoura'])

    if escolhaUsuario == escolhaComputador:
        mensagem = f'''
            Voce: {escolhaUsuario.upper()}
            Computador: {escolhaComputador.upper()}
            Resultado: EMPATE!!
        '''
    elif (escolhaUsuario == 'Pedra' and escolhaComputador == 'Tesoura') \
    or (escolhaUsuario == 'Papel' and escolhaComputador == 'Pedra') \
    or (escolhaUsuario == 'Tesoura' and escolhaComputador == 'Papel'):
        mensagem = f'''
        Voce: {escolhaUsuario.upper()}
        Computador: {escolhaComputador.upper()}
        Resultado: GANHOU!!
        '''
    else:
        mensagem = f'''
        Voce: {escolhaUsuario.upper()}
        Computador: {escolhaComputador.upper()}
        Resultado: PERDEU!!
        '''

    resultado.config(text=mensagem)





janela = tk.Tk()

frame = LabelFrame(janela, text='Qual você escolhe? ')
frame.pack()

iconePedra = PhotoImage(file='Python/Icones/rock.png')
iconePapel = PhotoImage(file='Python/Icones/paper.png')
iconeTesoura = PhotoImage(file='Python/Icones/scissor.png')

Button(frame, text='Pedra', command=escolheuPedra, image=iconePedra, compound=tk.LEFT).grid(column=0, row=1)
Button(frame, text='Papel',command=escolheuPapel, image= iconePapel, compound=tk.LEFT).grid(column=1, row=1)
Button(frame, text='Tesoura',command=escolheuTesoura, image= iconeTesoura, compound=tk.LEFT).grid(column=2, row=1)

resultado = Label(frame, pady=10, padx=10, justify=tk.LEFT)
resultado.grid(column = 0, row = 2, columnspan = 3)

janela.title('Pedra,Papel e Tesoura')
janela.geometry("500x500")
janela.mainloop() 

