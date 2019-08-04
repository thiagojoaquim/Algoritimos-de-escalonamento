from processo import Processos
import sys
from utilitarios import Util

sys.setrecursionlimit(1000000)


class Escalonamento():
    def __init__(self, alfa: int, processos: list()):
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

    def aprontarNovoProcesso(self):

        if (len(self.bloqueados) > 0):
            for processo in self.bloqueados:
                if (processo.current_blocked_time == 0):
                    processos_ativos = len(self.bloqueados) + len(self.prontos)
                    if (processos_ativos < self.alfa):
                        self.prontos.append(processo)
                        self.bloqueados.remove(processo)

            if (len(self.todos_processos) > 0):
                self.prontos.append(self.todos_processos[0])
                del self.todos_processos[0]

    def bloquear(self):
        self.execucao.bloquear()
        self.bloqueados.append(self.execucao)

        if (len(self.bloqueados) > 0):
            self.decrementarBloqueio()

    def decrementarBloqueio(self):
        for processo in self.bloqueados:
            processo.decrementarTempoBloqueio()
            # print("processo: " + str(processo.id_process) + ": "+ str(processo.current_blocked_time))

    def carregarFilas(self):
        self.prontos = self.todos_processos[0:self.alfa - 1]
        del self.todos_processos[0:self.alfa - 1]

    def executar(self, funcaoDeSelecao):
        self.carregarFilas()

        while (len(self.bloqueados) + len(self.prontos) + len(self.todos_processos)) > 0:
            # print("Total de processos Prontos: " + str (len(self.prontos)) + "\n")
            # print("Total de processos Bloqueados: " + str (len(self.bloqueados)) + "\n")

            if (len(self.prontos) > 0):
                print("prontos: " + str(len(self.prontos)))
                self.execucao = funcaoDeSelecao(self.prontos)
                self.prontos.remove(self.execucao)
                print("Executando processo ID: " + str(self.execucao.id_process) + "\n")
                tempoRestante = self.execucao.executar()
                print("para ID: " + str(self.execucao.id_process) + " falta:  " + str(tempoRestante))
                if (tempoRestante > 0):
                    self.bloquear()
                else:
                    self.__total_turnarond += 1
                    self.execucao = None
                    self.aprontarNovoProcesso()
            else:
                self.decrementarBloqueio()
                self.aprontarNovoProcesso()
                continue

        print(self.__total_turnarond)

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

