from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

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

texto = [] #lista quer será utilizada para manipulação das strings enviadas pelos botões
class MainApp(MDApp):
    def build(self):
        Window.size = (350, 500)
        return Builder.load_string(kv) 

    def inserir_texto(self,texto_botao):
        #aqui receberei o valor do botão como argumento, adicionarei a lista e tratarei a lista usando o join para que forme um texte que
        #será adicionado a um MDLabel dentro de um MDCard
        texto.append(texto_botao.text)
        self.root.ids.texto_calculadora.text = ''.join(texto)
           
       


    def apagar(self):
        #Para apagar algum valor
        if len(texto) > 1: #verifiquei se ele é maior que um para que apague apenas o ultimo valor por vez
            texto.pop(len(texto)-1)
            self.root.ids.texto_calculadora.text = ''.join(texto) # e após ser apagado o ultimo item na lista será adicionado uma nova string contendo os valores restante 
        else:
            #caso seja igual a 1 ou 0 apenas irei substituir o texto e limpar a lista
            texto.clear()
            self.root.ids.texto_calculadora.text = ''

    

    def soma(self,n1,n2):
        resultado = n1+n2
        return resultado
    def subtracao(self,n1,n2):
        resultado = n1-n2
        return resultado

    def mutiplicacao(self,n1,n2):
        return n1*n2
        
    def divisao(self,n1,n2):
        return n1/n2  
        
    def novo_numero(self,resultado):
        #Nesta função estarei recebendo o resultado da operação, limpando a lista, adicionado o novo item e adicionando o novo texto
        texto.clear()
        texto.append(str(int(resultado)))
        self.root.ids.texto_calculadora.text = ''.join(texto)
    def identificador(self):
        #Nesta função irei vericiar através de tratamento de string qual a operação está sendo feita e fazendo-a
        #todos as variaveis de resultado recebem os valores que ficam antes e depois do sinal de operação
        dentro_do_card =  self.root.ids.texto_calculadora.text
        if '+' in dentro_do_card:
            resultado_soma = self.soma(int(''.join(texto[0:texto.index('+')])),int(''.join(texto[texto.index('+'):]))) 
            self.novo_numero(resultado_soma)
        if '-' in dentro_do_card:
            resultado_subtracao = self.subtracao(int(''.join(texto[0:texto.index('-')])),int(''.join(texto[texto.index('-')+1:])))
            self.novo_numero(resultado_subtracao)
            
        if '*' in dentro_do_card:
            resultado_mutiplicacao = self.mutiplicacao(int(''.join(texto[0:texto.index('*')])),int(''.join(texto[texto.index('*')+1:])))
            self.novo_numero(resultado_mutiplicacao)

        if '/' in dentro_do_card:
            resultado_divisao = self.divisao(int(''.join(texto[0:texto.index('/')])),int(''.join(texto[texto.index('/')+1:])))
            self.novo_numero(resultado_divisao)

        
        

MainApp().run()
