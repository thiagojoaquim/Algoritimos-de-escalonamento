from algoritmos import Escalonamento
from random import randint
from utilitarios import Util
from processo import Processos
import sys

class Garantido(Escalonamento.Escalonamento):
    def __init__(self, alfa:int, processos:list(), quantum:int):
        super().__init__(alfa, processos, quantum, True)




    def funcaoDeSelecao(self, lista:list):
        retorno = lista[0]
        for processo in lista :
            if(processo.waiting_time > retorno.waiting_time):
                retorno = processo
        return processo


    def executar(self):
        super().executar(self.funcaoDeSelecao)

