from tkinter import Tk,Label, Text, Button
import matplotlib.pyplot as plt


def contar_palavras():
    lista_texto = texto.get('1.0', 'end-1c').replace(","," ").lower().split()
    resultado = lambda x: lista_texto.count(x)
    palavras = map(resultado, lista_texto)
    palavras_unicas =  dict(zip(lista_texto, palavras))
    plt.bar(palavras_unicas.keys(), palavras_unicas.values())
    plt.title("Contador de Palavras")
    plt.xlabel("Palavras")
    plt.ylabel("Frequência")
    plt.show()



win = Tk()
win.title("Contador de Palavras")

label = Label(win, text="Digite ou cole o texto:")
texto = Text(win, height=10, width=50)
botao = Button(win, text="Contar Palavras", command=contar_palavras)
novo_resultado = Label(win, text="Resultado:")

label.pack()
texto.pack()
botao.pack()
novo_resultado.pack()
win.geometry("400x300")
win.mainloop()