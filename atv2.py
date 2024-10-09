import tkinter as tk
import tkinter.messagebox as tkm


janela = tk.Tk()

janela.title("Interface gráfica com tkinter")

janela.geometry("500x300")

rotulo = tk.Label(janela, text="Bem vindo a sua primeira interface!")
rotulo.pack()

button = button(janela, text="Botão clicado!")

janela.mainloop()