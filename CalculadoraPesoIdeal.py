import PySimpleGUI

class TelaPython:
    def __init__(self):
        layout = [
            [PySimpleGUI.Text('Peso',size=(5,0)),PySimpleGUI.Input(size=(15,0),key='peso')],
            [PySimpleGUI.Text('Altura',size=(5,0)),PySimpleGUI.Input(size=(15,0),key='altura')],
            [PySimpleGUI.Text('Homem ou Mulher?')],
            [PySimpleGUI.Radio('Homem', 'sexo',key='homem'),PySimpleGUI.Radio('Mulher','sexo',key='mulher')],
            [PySimpleGUI.Button('Calcular imc')],
            [PySimpleGUI.Output(size=(20,3))],
            [PySimpleGUI.Text('              Tabela imc')],
            [PySimpleGUI.Text('IMC < 18,5 = Abaixo do peso')],
            [PySimpleGUI.Text('IMC > 18,5 < 24,9 = Peso normal')],
            [PySimpleGUI.Text('IMC > 25 < 29,9 = Sobrepeso')],
            [PySimpleGUI.Text('IMC > 30 = Obesidade')]

        ]
        self.janela = PySimpleGUI.Window("Calculadora IMC").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            peso = self.values['peso']
            altura = self.values['altura']
            sexo_homem = self.values['homem']
            sexo_mulher = self.values['mulher']
            calculo_peso = float(peso) 
            calculo_altura = float(altura) * float(altura)
            imc = float(calculo_peso) / float(calculo_altura) 
            print('Seu imc é de: ', imc)

tela = TelaPython()
tela.Iniciar()