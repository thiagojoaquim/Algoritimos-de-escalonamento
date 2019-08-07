from algoritmos import Escalonamento
from random import randint
from utilitarios import Util

import sys


class MultilevelFeedback(Escalonamento.Escalonamento):
    def __init__(self, alfa: int, processos: list(), quantumx: int, quantumy, quantumz):
        super().__init__(alfa, processos, quantumx, True)
        self.PrioridadeMaxima = -1
        self.quantumBaixo = quantumx
        self.quantumMedio = quantumy
        self.quantumAlto = quantumz

    def funcaoDeSelecao(self, lista):
        retorno = self.prontos[0]
        for processo in lista:
            if processo.id_process == self.PrioridadeMaxima:
                return processo
            if processo.prioridadeMultilevel > retorno.prioridadeMultilevel:
                retorno = processo
        if retorno.prioridadeMultilevel == 0:
            self.quantum = self.quantumBaixo
            retorno.prioridadeMultilevel = 1

        elif retorno.prioridadeMultilevel == 1:
            self.quantum = self.quantumMedio
            retorno.prioridadeMultilevel = 2

        else:
            self.quantum = 1
            self.PrioridadeMaxima = retorno.id_process
        return retorno



    def executar(self):
        super().executar(self.funcaoDeSelecao)



