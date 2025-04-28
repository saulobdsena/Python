import tkinter as tk
from tkinter import Label, Frame
import datetime
import time
import threading
import pygame

def tocar_alarme():
    pygame.mixer.init()
    pygame.mixer.music.load('/home/saulobdsena/GitHub/Python/Projetos/Sounds/somDespertador.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def alarme():
    setTempoAlarme = f'{hora.get()}:{minutos.get()}:{segundo.get()}'
    while True:
        time.sleep(1)
        horaLocal = datetime.datetime.now().strftime('%H:%M:%S')
        print(horaLocal, setTempoAlarme)
        if horaLocal == setTempoAlarme:
            threading.Thread(target=tocar_alarme).start()
            break

janela = tk.Tk()
janela.geometry("400x200")
janela.title('Alarme Python')

tk.Label(janela, text='Alarme', font=('Helvetica', 20, 'bold')).pack(pady=10)
tk.Label(janela, text='Definir Alarme').pack(pady=5)

frame = tk.Frame(janela)
frame.pack()

def opcoes(value):
    opc = tk.StringVar(janela)
    opcoes = [str(i).zfill(2) for i in range(value)]
    opc.set(opcoes[0])
    tk.OptionMenu(frame, opc, *opcoes).pack(side=tk.LEFT)
    return opc

hora = opcoes(24)
minutos = opcoes(60)
segundo = opcoes(60)

tk.Button(janela, text='Definir', font=('Helvetica', 15), command=lambda: threading.Thread(target=alarme).start()).pack(pady=20)

janela.mainloop()
