from processo import Processos
import sys

sys.setrecursionlimit(1000000)


class Escalonamento():
    def __init__(self, processos):
        self._processos = processos
        self._numero_de__processos = len(processos)
        self._total_turnarond = 0
        self._total_waiting_time = 0
        self._total_service_time = 0
        self._processor_utilization = 0


