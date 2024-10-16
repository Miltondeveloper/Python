import tkinter as tk
from tkinter.messagebox import showinfo

def mostrar_mensagem():
     showinfo("Informaçao", "Botão clicado!")
    


janela = tk.Tk()

janela.title("Interface gráfica com tkinter")

janela.geometry("500x300")

rotulo = tk.Label(janela, text="Bem vindo a sua primeira interface gráfica!")
rotulo.pack(pady=20)

button = tk.Button(janela, text="Clique aqui", command = mostrar_mensagem)
button.pack(pady=20)

janela.mainloop()
