import tkinter as tk
from tkinter.messagebox import showinfo

def show_message():
    showinfo("Informação", "Você ganhou o brasão da Coragem!!!")
    
def show_message2():
    showinfo("Informação", "Você ganhou o brasão da Amizade!!!")

window = tk.Tk()

window.title("Qual você escolhe???")

window.geometry("800x750")

imagem = tk.PhotoImage(file="digimon.png")

rotulo = tk.Label(window, image=imagem)
rotulo.pack()

button = tk.Button(window, text="Wargreymon", command= show_message)
button.pack(padx=100, pady=20)
button.place()

button = tk.Button(window, text="MetalGarurumon", command=show_message2)
button.pack(padx=50, pady=10)

window.mainloop()
