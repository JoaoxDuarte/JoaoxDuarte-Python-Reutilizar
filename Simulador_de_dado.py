from lib2to3.pgen2 import pgen
from random import Random

import random
import PySimpleGUI as pg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
               #self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '
        #theme 
        pg.theme('DarkAmber')
        #layout
        self.layout = [
            [pg.Text('Jogar o dado? ')],
            [pg.Button('sim'),pg.Button('não')]
        ]

    def Iniciar(self):
        #Criar Janela
        self.janela = pg.Window('Simulador de Dado',layout=self.layout)
        #Ler os valores na tela
        self.eventos, self.valores = self.janela.Read()
        # fazer algo com esses valores
                                 # self.eventos = input(self.mensagem)
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agredecemos sua participação')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua self.eventos')
        

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()