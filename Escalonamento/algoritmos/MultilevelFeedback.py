from algoritmos import Escalonamento
from random import randint
from utilitarios import Util

import sys


class MultilevelFeedback(Escalonamento.Escalonamento):
    def __init__(self, alfa: int, processos: list(), quantum: int):
        super().__init__(alfa, processos, quantum, True)
        self.PrioridadeMaxima = -1

    def funcaoDeSelecao(self, lista):
        retorno = self.prontos[0]
        for processo in lista:
            if processo.id_process == self.PrioridadeMaxima:
                return processo
            if processo.prioridadeMultilevel > retorno.prioridadeMultilevel:
                retorno = processo
        if retorno.prioridadeMultilevel == 0:
            self.quantum = 2
            retorno.prioridadeMultilevel = 1

        elif retorno.prioridadeMultilevel == 1:
            self.quantum = 4
            retorno.prioridadeMultilevel = 2

        else:
            self.quantum = 6
            self.PrioridadeMaxima = retorno.id_process
        return retorno



    def executar(self):
        super().executar(self.funcaoDeSelecao)


a = MultilevelFeedback(100, Util.carregar()[0:20], 1)


a.executar()
