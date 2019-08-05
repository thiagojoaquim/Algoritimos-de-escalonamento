from algoritmos import Escalonamento
from random import randint
from utilitarios import Util
from processo import Processos
import sys

class Garantido(Escalonamento.Escalonamento):
    def __init__(self, alfa:int, processos:list(), beta:int):
        super().__init__(alfa, processos, beta)



    def funcaoDeSelecao(self, lista:list):
        return lista[0]

    def executar(self):
        super().executar(self.funcaoDeSelecao)
