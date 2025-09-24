# 🧠 Contador de Palavras com Interface Gráfica

Este é um projeto simples feito com **Python + Tkinter** que conta a frequência de palavras em um texto e exibe o resultado em um gráfico de barras usando o **Matplotlib**. Ideal pra quem quer brincar com interfaces gráficas e análise de texto rapidinho!

---


## 💡 Funcionalidades

- 📝 Campo para digitar ou colar um texto qualquer.
- 📊 Conta quantas vezes cada palavra aparece.
- 📉 Exibe os dados em um gráfico de barras com `matplotlib`.

---

## 🧩 Código-fonte

```python
### 🧩 Código-fonte comentado passo a passo

#### 1. Importações

```python
from tkinter import Tk, Label, Text, Button
import matplotlib.pyplot as plt
```

- `tkinter`: biblioteca padrão do Python para criar interfaces gráficas.
- `matplotlib.pyplot`: usado para gerar o gráfico de barras com as palavras e suas frequências.

---

#### 2. Função principal `contar_palavras`

```python
def contar_palavras():
    lista_texto = texto.get('1.0', 'end-1c').replace(",", " ").lower().split()
    resultado = lambda x: lista_texto.count(x)
    palavras = map(resultado, lista_texto)
    palavras_unicas = dict(zip(lista_texto, palavras))
    
    plt.bar(palavras_unicas.keys(), palavras_unicas.values())
    plt.title("Contador de Palavras")
    plt.xlabel("Palavras")
    plt.ylabel("Frequência")
    plt.show()
```

- **`texto.get('1.0', 'end-1c')`**: captura todo o conteúdo digitado na caixa de texto.
- **`.replace(",", " ")`**: substitui vírgulas por espaços para não atrapalhar a separação das palavras.
- **`.lower().split()`**: transforma tudo em minúsculo e separa por espaços.
- **`lambda x: lista_texto.count(x)`**: função anônima que conta quantas vezes uma palavra aparece.
- **`map(...)`**: aplica essa função a cada palavra.
- **`zip(...)` + `dict(...)`**: junta as palavras com suas contagens em um dicionário.
- **`plt.bar(...)`**: cria o gráfico de barras.
- **`plt.show()`**: exibe o gráfico na tela.

---

#### 3. Criando a janela principal com os widgets

```python
win = Tk()
win.title("Contador de Palavras")
```

- Cria a janela da aplicação e define seu título.

---

#### 4. Componentes da interface

```python
label = Label(win, text="Digite ou cole o texto:")
texto = Text(win, height=10, width=50)
botao = Button(win, text="Contar Palavras", command=contar_palavras)
novo_resultado = Label(win, text="Resultado:")
```

- `Label`: texto explicativo para o usuário.
- `Text`: caixa onde o usuário digita ou cola o texto.
- `Button`: botão que chama a função `contar_palavras`.
- Outro `Label`: pode ser usado para exibir resultados ou status (aqui estático).

---

#### 5. Exibindo os componentes na tela

```python
label.pack()
texto.pack()
botao.pack()
novo_resultado.pack()
```

- `pack()`: método usado para posicionar os widgets verticalmente.

---

#### 6. Tamanho da janela e loop principal

```python
win.geometry("400x300")
win.mainloop()
```

- Define o tamanho da janela: 400px de largura por 300px de altura.
- `mainloop()`: inicia o loop da interface, mantendo a janela aberta.

