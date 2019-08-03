from processo import Processos
from algoritmos import Escalonamento
import utilitarios
import sys

class Prioridade(Escalonamento):
    def __init__(self, process):
        Escalonamento.__init__(self, process)

    def executePrioridadeEscalonamento(self):
        for i in range(0, self.numero_de_processos):
            process = self.find_Prioridade()

            self._total_turnarond += int(process.time_execution)
        print(str(self._total_turnarond / 1000) + "ms")




