import tkinter as tk
from tkinter import Label, Frame


janela = tk.Tk()

tk.Label(frame, text='Alarme Pythônico', pady=40).grid(column=1, row=1, columnspan=2)
frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1)

janela.title('Alarme Python')
janela.mainloop