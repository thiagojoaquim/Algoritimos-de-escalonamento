from algoritmos import Escalonamento
from random import randint
from utilitarios import Util
from processo import Processos
import sys

class HRRN(Escalonamento.Escalonamento):
    def __init__(self, alfa:int, processos:list()):
        super().__init__(alfa, processos)



    def funcaoDeSelecao(self, lista:list):
        selecionado = lista[0]
        responseRatio = 0
        for processo in lista:
            if(responseRatio < (processo.waiting_time + processo.time_execution)/processo.time_execution):
                selecionado = processo
                responseRatio = (processo.waiting_time + processo.time_execution)/processo.time_execution
        return selecionado






    def executar(self):
        super().executar(self.funcaoDeSelecao)


a = HRRN(100, Util.carregar()[0:100])
a.executar()