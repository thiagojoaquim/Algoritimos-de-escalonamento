from algoritmos import Escalonamento
from algoritmos import RR
from random import randint
from utilitarios import Util

import sys


class StateDependent(RR.RR):
    def __init__(self, alfa: int, processos: list(), quantum: int):
        super().__init__(alfa, processos, quantum)
        self.PrioridadeMaxima = -1
        self.quantumPadrao = quantum

    def funcaoDeSelecao(self, lista):
        retorno = super().funcaoDeSelecao(lista)
        self.quantum = int(self.quantumPadrao / len(self.prontos))
        return retorno

    def executar(self):
        super().executar(self.funcaoDeSelecao)


