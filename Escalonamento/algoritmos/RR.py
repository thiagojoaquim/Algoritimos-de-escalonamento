from algoritmos import Escalonamento
from random import randint
from utilitarios import Util

import sys


class RR(Escalonamento.Escalonamento):
    def __init__(self, alfa: int, processos: list(), quantum: int):
        super().__init__(alfa, processos, quantum, True)
        self.filaDeProcessados = list()

    def atualizarFilaDeProcessados(self):
        for processo in self.prontos:
            if not processo in self.filaDeProcessados:
                self.filaDeProcessados.append(processo)
        for processo in self.filaDeProcessados:
            if not processo in self.prontos:
                self.filaDeProcessados.remove(processo)

    def funcaoDeSelecao(self, lista):
        self.atualizarFilaDeProcessados() #Verifica se novos processos entraram na fila
        retorno = self.filaDeProcessados[0]
        #self.filaDeProcessados.remove(retorno)
        ##   self.filaDeProcessados.append(retorno)
        return retorno



    def executar(self, funcaoDeSelecao):
        if funcaoDeSelecao is None:
            super().executar(self.funcaoDeSelecao)
        else:
            super().executar(funcaoDeSelecao)


