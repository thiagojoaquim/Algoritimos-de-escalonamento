from processo import Processos
import sys
from utilitarios import Util

sys.setrecursionlimit(1000000)


class Escalonamento():
    def __init__(self, alfa: int, processos: list(), beta: int):
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
        self.beta = beta
        self.max_processos_em_execucao =  1
        self.isExecutando = False
        self.tempo = 0

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
        while (len(self.todos_processos) > 0 and (len(self.bloqueados) + len(self.prontos)) < self.alfa):
            #print("aaa")
            if self.todos_processos.submission_time <= self.tempo:
                self.prontos.append(self.todos_processos[0])
                del self.todos_processos[0]
            else:
                break

    def bloquear(self):
        self.bloqueados.append(self.execucao)

        if (len(self.bloqueados) > 0):
            self.decrementarBloqueio()

    def decrementarBloqueio(self):
        for processo in self.bloqueados:
            processo.decrementarTempoBloqueio(self.beta)
            # print("processo: " + str(processo.id_process) + ": "+ str(processo.current_blocked_time))

    def carregarFilas(self):
        self.prontos = self.todos_processos[0:self.alfa - 1]
        del self.todos_processos[0:self.alfa - 1]

    def esperar(self):
        for processo in self.prontos:
            processo.esperar()
        for processo in self.bloqueados:
            processo.esperar()

    def imprimir(self):
        print("prontos: " + str(len(self.prontos)))
        print("bloqueados: " + str(len(self.bloqueados)))
        print("todos: " + str(len(self.todos_processos)))
        print("Executando processo ID: " + str(self.execucao.id_process) + "\n")

    def processar(self, funcaoDeSelecao):
        self.execucao = funcaoDeSelecao(self.prontos)
        self.imprimir()
        self.prontos.remove(self.execucao)
        self.__tempo_total_de_espera += self.execucao.waiting_time
        tempoRestante = self.execucao.executar(self.beta)
        self.__total_service_time += 1
        print("para ID: " + str(self.execucao.id_process) + " falta:  " + str(tempoRestante))
        if (tempoRestante > 0):
            self.bloquear()
        else:
            self.execucao = None
            #self.escalonamentoMedioPrazo()

    def escrever(self):
        resp = ("Tempo de Espera total: " + str(self.__tempo_total_de_espera) + "\n") \
               + ("Tempo de Espera Média: " + str(self.__tempo_total_de_espera / self.numeroDeProcessos)+ "\n") \
               + ("Tempo de Servico Total:" + str(self.__total_service_time)+ "\n") + \
               ("Tempo de servico Médio: " + str(self.__total_service_time / self.numeroDeProcessos)+ "\n")
        Util.escrever(resp)

    def executar(self, funcaoDeSelecao):
        self.carregarFilas()
        tempo = int(0)
        # ENQUANTO EXISTIR PROCESSO PARA SER PROCESSADO
        while (len(self.bloqueados) + len(self.prontos) + len(self.todos_processos)) > 0:
            tempoRestante = None
            self.tempo += 1
            self.decrementarBloqueio()
            self.esperar()
            if len(self.prontos) > 0 and not self.isExecutando:
                self.execucao = funcaoDeSelecao(self.prontos)
                self.isExecutando = True
                self.imprimir()
                self.prontos.remove(self.execucao)
                tempoRestante = self.execucao.executar(self.beta)
                self.__total_service_time += 1
                print("para ID: " + str(self.execucao.id_process) + " falta:  " + str(tempoRestante))
                if tempoRestante <= 0:
                    self.execucao = None
                    self.isExecutando = False
                else:
                    if self.execucao.blocked_time > 0:
                        self.bloquear()
                        self.execucao = None
                        self.isExecutando = False

            elif self.isExecutando:
               tempoRestante = self.execucao.executar(self.beta)
               if tempoRestante <= 0:
                   self.execucao = None
                   self.isExecutando = False
               else:
                   if self.execucao.blocked_time > 0:
                       self.bloquear()
                       self.execucao = None
                       self.isExecutando = False
               self.__total_service_time += 1
            else:
                self.escalonamentoMedioPrazo()
        print(self.__total_turnarond)
        print("Tempo de Espera total: " + str(self.__tempo_total_de_espera))
        print("Tempo de Espera Média: " + str(self.__tempo_total_de_espera / self.numeroDeProcessos))
        print("Tempo de Servico Total:" + str(self.__total_service_time))
        print("Tempo de servico Médio: " + str(self.__total_service_time / self.numeroDeProcessos))

    def test(self):
        self.bloqueados = self.todos_processos[0:10]
        for processo in self.bloqueados:
            processo.bloquear()
        while (len(self.bloqueados) > 0):
            self.decrementarBloqueio()


def funcao(lista):
    if (len(lista) <= 0):
        return None
    resp = lista[0]
    del lista[0]
    return resp
