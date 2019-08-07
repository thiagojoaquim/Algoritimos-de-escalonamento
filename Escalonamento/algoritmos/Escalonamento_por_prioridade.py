from processo import Processos
from algoritmos import Escalonamento
from utilitarios import Util
from processo import Processos
import utilitarios
import sys


class Prioridade(Escalonamento.Escalonamento):
    def __init__(self, alfa:int, processos:list() , quantum:int):
        super().__init__(alfa, processos , quantum, True)

    def funcaoDeSelecao(self, lista):
        maiorPrioridade = lista[0]
        for i in range(0, len(lista)):
            if maiorPrioridade.priority < lista[i].priority:
                maiorPrioridade = lista[i]
        return maiorPrioridade

    def executar(self):
        super().executar(self.funcaoDeSelecao)



