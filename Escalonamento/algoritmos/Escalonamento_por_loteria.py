from algoritmos import Escalonamento
from random import randint
from utilitarios import Util
from processo import Processos
import sys

class Loteria(Escalonamento.Escalonamento):
    def __init__(self, alfa:int, processos:list(), quantum:int):
        super().__init__(alfa, processos, quantum, False)



    def funcaoDeSelecao(self, lista:list):
        return lista[randint(0, len(lista) - 1)]



    def executar(self):
        super().executar(self.funcaoDeSelecao)


