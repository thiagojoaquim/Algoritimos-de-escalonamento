from processo import Processos
import sys
from utilitarios import Util

sys.setrecursionlimit(1000000)


class Escalonamento():
    def __init__(self, alfa: int, processos: list(), quantum: int, isPreemptivo: bool):
        self.numeroDeProcessos = len(processos)
        self.__todos_processos = processos
        self.__total_turnarond = 0
        self.__tempo_total_de_espera = 0
        self.__total_service_time = 0
        self.__processor_utilization = 0
        self.__alfa = alfa
        self.__prontos = list()
        self.__bloqueados = list()
        self.__execucao = Processos.Processos
        self.__total_processos_ativos = 0
        self.quantum = quantum
        self.max_processos_em_execucao = 1
        self.isExecutando = False
        self.tempo = int(0)
        self.isPreemptivo = isPreemptivo
        self.tempo_de_resposta_total = int(0)

    @property
    def total_processos_ativos(self):
        return self.__total_processos_ativos

    @total_processos_ativos.setter
    def total_processos_ativos(self, n):
        self.__total_processos_ativos = n

    @property
    def todos_processos(self):
        return self.__todos_processos

    @todos_processos.setter
    def id_process(self, todos_processos):
        self.__todos_processos = todos_processos

    @property
    def alfa(self):
        return self.__alfa

    @alfa.setter
    def alfa(self, alfa: int):
        self.__alfa = alfa

    @property
    def execucao(self):
        return self.__execucao

    @execucao.setter
    def execucao(self, execucao):
        self.__execucao = execucao

    @property
    def prontos(self):
        return self.__prontos

    @prontos.setter
    def prontos(self, prontos):
        self.__prontos = prontos

    @property
    def bloqueados(self):
        return self.__bloqueados

    @bloqueados.setter
    def bloqueados(self, bloqueados):
        self.__bloqueados = bloqueados

    def escalonamentoMedioPrazo(self):

        if (len(self.bloqueados) > 0):
            for processo in self.bloqueados:
                if (processo.blocked_time <= 0):
                    # print("processo: " + str(processo.id_process) + ": "+ str(processo.current_blocked_time)
                    self.prontos.append(processo)
                    self.bloqueados.remove(processo)
        i = int(0)
        sair = False
        if (len(self.todos_processos) > 0 and (len(self.bloqueados) + len(self.prontos)) < self.alfa and not sair):
            for processo in self.todos_processos:
                if int(self.todos_processos[i].submission_time) <= int(self.tempo) and len(self.prontos) + len(self.bloqueados) < self.alfa:
                    self.prontos.append(self.todos_processos[0])
                    del self.todos_processos[0]
                else:
                    sair = True
                    break

    def bloquear(self):
        self.bloqueados.append(self.execucao)

        if (len(self.bloqueados) > 0):
            self.decrementarBloqueio()

    def decrementarBloqueio(self):
        for processo in self.bloqueados:
            processo.decrementarTempoBloqueio(self.quantum)
            # print("processo: " + str(processo.id_process) + ": "+ str(processo.current_blocked_time))

    def carregarFilas(self):
        self.todos_processos.sort()

    def esperar(self):
        for processo in self.prontos:
            processo.esperar(self.quantum)
        for processo in self.bloqueados:
            processo.esperar(self.quantum)

    def imprimir(self):
        print("prontos: " + str(len(self.prontos)))
        print("bloqueados: " + str(len(self.bloqueados)))
        print("todos: " + str(len(self.todos_processos)))
        print("Executando processo ID: " + str(self.execucao.id_process) + "\n")

    def escrever(self):
        resp = "Tempo: " + str(self.tempo) + ("Tempo de Espera total: " + str(self.__tempo_total_de_espera)) \
               +("Tempo de Espera Média: " + str(self.__tempo_total_de_espera / self.numeroDeProcessos))\
               +("Tempo de Servico Total: " + str(self.__total_service_time))\
               +("Tempo de servico Médio: " + str(self.__total_service_time / self.numeroDeProcessos))\
               +("Tempo de Retorno Médio: " + str(self.__total_turnarond / self.numeroDeProcessos))\
               +("Tempo de Resposta Médio: " + str(self.tempo_de_resposta_total / self.numeroDeProcessos))\
               +("Utilização do processador: " + str((self.__total_service_time / self.tempo) * 100) + "%")\
               +("Throughput(Um processo é executado a cada): " + str(  int(self.tempo) / self.numeroDeProcessos  ))
        Util.escrever(resp)

    def executar(self, funcaoDeSelecao):
        self.carregarFilas()  # Ordena processos com base na submissão
        tempo = int(0)
        # ENQUANTO EXISTIR PROCESSO PARA SER PROCESSADO
        while (len(self.bloqueados) + len(self.prontos) + len(self.todos_processos)) > 0:
            self.escalonamentoMedioPrazo()
            tempoRestante = None
            self.tempo += self.quantum
            self.decrementarBloqueio()
            self.esperar()
            if len(self.prontos) > 0 and not self.isExecutando:
                self.execucao = funcaoDeSelecao(self.prontos)
                self.isExecutando = True
                self.imprimir()
                self.prontos.remove(self.execucao)
                tempoRestante = self.execucao.executar(self.quantum)
                self.tempo += self.quantum - 1
                self.__total_service_time += self.quantum
                print("para ID: " + str(self.execucao.id_process) + " falta:  " + str(tempoRestante))
                if tempoRestante <= 0:
                    self.__tempo_total_de_espera += self.execucao.waiting_time
                    self.execucao.return_time += self.execucao.waiting_time
                    self.__total_turnarond += self.execucao.return_time
                    self.execucao.response_time = self.tempo - int(self.execucao.submission_time)
                    self.tempo_de_resposta_total += self.execucao.response_time
                    self.execucao = None
                    self.isExecutando = False
                else:
                    if self.execucao.blocked_time > 0:
                        self.bloquear()
                        self.execucao = None
                        self.isExecutando = False


            elif self.isExecutando:

                if self.isPreemptivo and len(self.prontos) > 0:
                    listaux = list()
                    listaux.append(self.execucao)
                    proximo = funcaoDeSelecao([self.execucao, funcaoDeSelecao(self.prontos)])
                    if proximo.id_process != self.execucao.id_process:
                        if len(self.prontos) + len(self.bloqueados) < 100:
                            self.prontos.append(self.execucao)
                        else:
                            self.todos_processos.append(self.execucao)
                        self.execucao = proximo
                        self.prontos.remove(proximo)

                tempoRestante = self.execucao.executar(self.quantum)
                self.tempo += self.quantum - 1
                self.__total_service_time += self.quantum
                print("para ID: " + str(self.execucao.id_process) + " falta:  " + str(tempoRestante))
                if tempoRestante <= 0:
                    self.__tempo_total_de_espera += self.execucao.waiting_time
                    self.execucao.return_time += self.execucao.waiting_time
                    self.__total_turnarond += self.execucao.return_time
                    self.execucao.response_time = self.tempo - int(self.execucao.submission_time)
                    self.tempo_de_resposta_total += self.execucao.response_time
                    self.execucao = None
                    self.isExecutando = False
                else:
                    if self.execucao.blocked_time > 0:
                        self.bloquear()
                        self.execucao = None
                        self.isExecutando = False


        print("Tempo: " + str(self.tempo))
        print("Tempo de Espera total: " + str(self.__tempo_total_de_espera))
        print("Tempo de Espera Média: " + str(self.__tempo_total_de_espera / self.numeroDeProcessos))
        print("Tempo de Servico Total: " + str(self.__total_service_time))
        print("Tempo de servico Médio: " + str(self.__total_service_time / self.numeroDeProcessos))
        print("Tempo de turnaround Médio: " + str(self.__total_turnarond / self.numeroDeProcessos))
        print("Tempo de Resposta Médio: " + str(self.tempo_de_resposta_total / self.numeroDeProcessos))
        print("Utilização do processador: " + str((self.__total_service_time / self.tempo) * 100) + "%")
        print("Throughput(Um processo é executado a cada): " + str(  int(self.tempo) / self.numeroDeProcessos  ))
