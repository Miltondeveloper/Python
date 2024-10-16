import tkinter as tk
from tkinter.messagebox import showinfo

def show_message():
    showinfo("Informação", "Goku is the best!!!")

window = tk.Tk()

window.title("Kakarotto")

window.geometry("800x800")

imagem = tk.PhotoImage(file="goku.png")

rotulo = tk.Label(window, image=imagem)
rotulo.pack()

button = tk.Button(window, text="Goku ou Saitama???", command= show_message)
button.pack(pady=10)

window.mainloop()

