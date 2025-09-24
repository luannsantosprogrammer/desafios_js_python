# Calculadora Python com KivyMD

Esta é uma calculadora simples que oferece cálculos um de cada vez, utilizando os quatro principais operadores.

Utilizando **Python**, o framework **Kivy** e o material design do **KivyMD**, desenvolvi a GUI de forma prática, rápida e estilosa.

## Estrutura KV

Nesta estrutura KV, adiciono os widgets que enviam e recebem comandos para a lógica dentro da estrutura de código Python.

```python
kv = '''

MDBoxLayout:
    orientation: "vertical"
    spacing: 10

    MDTopAppBar:
        title: "CALCULADORA PYTHON"
        size_hint_y: .3
    MDCard:
        style: "elevated"
        
        MDLabel:
            id: texto_calculadora
            text: ""
            font_size:"48sp"
            halign:"center"
            
    
    
    MDBoxLayout:
        pos_hint: {"center_x": .55,"center_y":.1}
        size_hint_x: 1
        size_hint_y: 1.5

        orientation: "vertical"

        MDGridLayout:
            pos_hint: {"center_x":.5}
            spacing: 20
            cols: 4
            rows: 1
            MDRaisedButton:
                text: "1" 
                id: um
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "2" 
                id: dois 
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "3"
                id: tres
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "+"
                id: soma
                on_release: app.inserir_texto(self)

        MDGridLayout:
            cols: 4
            rows: 1
            pos_hint: {"center_x":.5}
            spacing: 20
           
            MDRaisedButton:
                text: "4"
                id : quatro
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "5"
                id: cinco
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "6"
                id: seis
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "-"
                id: subtracao 
                on_release: app.inserir_texto(self) 

        MDGridLayout:
            cols: 4
            rows: 1
            pos_hint: {"center_x":.5}
            spacing: 20
            
            MDRaisedButton:
                text: "7"
                id: sete
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "8"
                id:oito
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "9"
                id:nove  
                on_release: app.inserir_texto(self)  
            MDRaisedButton:
                text: "*"
                id: mutiplicacao
                on_release: app.inserir_texto(self)
                
        MDGridLayout:
            cols: 4
            rows: 1
            pos_hint: {"center_x":.5}
            spacing: 20
            MDRaisedButton:
                text: "DEL"
                id: cancelar
                on_release: app.apagar()
                
            MDRaisedButton:
                text: "0"
                id: zero
                on_release: app.inserir_texto(self)
            MDRaisedButton:
                text: "="
                on_release: app.identificador()
                
            MDRaisedButton:
                text: "/"
                id: divisao
                on_release: app.inserir_texto(self)
'''
