from processo import Processos
import sys
sys.setrecursionlimit(1000000)


class Scheduling():
    def __init__(self, processes):
        self._processes = processes
        self._number_of_processes = len(processes)
        self._total_turnarond = 0
        self._total_waiting_time = 0
        self._total_service_time = 0
        self._processor_utilization = 0

class Priority(Scheduling):
     def __init__(self, process):
        Scheduling.__init__(self, process)

     def executePriorityScheduling(self):
        for i in range(0, self._number_of_processes):
            process = self.find_priority()
            self._total_turnarond += int (process.time_execution)
        print(str(self._total_turnarond / 1000) + "ms")



     def find_priority(self):
        processaux = self._processes[0]
        for process in self._processes:
                if process.priority > processaux.priority:
                        processaux = process
        self._processes.remove(processaux)
        return processaux

def carregar():
        file = open("cenario1.txt")
        cenario = file.read()
        cenario = cenario.split("\n")
        cenario = cenario[0:1]
        processes = []
        for c in cenario:
            c = c.split(',')
            if c != ['']:
                aux = Processos.Processos(c[0], c[1], c[2], c[3], c[4])
                processes.append(aux)
        return processes






escalonamento = Priority(carregar())
escalonamento.executePriorityScheduling()

