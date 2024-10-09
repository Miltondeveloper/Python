import tkinter as tk

janela = tk.Tk()

janela.title("Interface gráfica com tkinter")

janela.geometry("500x300")

rotulo = tk.Label(janela, text="Bem vindo a sua primeira interface gráfica!")
rotulo.pack()

janela.mainloop()