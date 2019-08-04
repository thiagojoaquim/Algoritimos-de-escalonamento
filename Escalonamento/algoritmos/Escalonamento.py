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
        self.beta = 1

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
                    # print("processo: " + str(processo.id_process) + ": "+ str(processo.current_blocked_time))
                    processos_ativos = len(self.bloqueados) + len(self.prontos)
                    if (processos_ativos <= self.alfa):
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


    def executar(self, funcaoDeSelecao):
        self.carregarFilas()
        #ENQUANTO EXISTIR PROCESSO PARA SER PROCESSADO
        while (len(self.bloqueados) + len(self.prontos) + len(self.todos_processos)) > 0:
            # print("Total de processos Prontos: " + str (len(self.prontos)) + "\n")
            # print("Total de processos Bloqueados: " + str (len(self.bloqueados)) + "\n")
            self.decrementarBloqueio()
            #SE EXISTIR PROCESSO PRONTO
            if (len(self.prontos) > 0):
                print("prontos: " + str(len(self.prontos)))
                print("bloqueados: " + str(len(self.bloqueados)))
                print("todos: " + str(len(self.todos_processos)))
                #APLICANDO FUNÇÃO DE SELEÇÃO PARA RESGATAR O PROCESSO A SER EXECUTADO PELO PROCESSADOR
                self.execucao = funcaoDeSelecao(self.prontos)
                self.esperar()
                #REMOVENDO DA LISTA DE PRONTOS
                self.prontos.remove(self.execucao)
                print("Executando processo ID: " + str(self.execucao.id_process) + "\n")
                #FUNCAO EXECUTAR DECREMENTA O TEMPO DE EXECUÇÃO E RETORNA O TEMPO DE EXECUÇAO RESTANTE
                tempoRestante = self.execucao.executar(self.beta)
                self.__total_service_time += 1
                print("para ID: " + str(self.execucao.id_process) + " falta:  " + str(tempoRestante))
                #SE AINDA NÃO TERMINOU DE SER EXECUTADO BLOQUEIO O PROCESSO
                # A FUNÇÃO BLOQUEAR DEFINE O TEMPO DE BLOQUEIO ATUAL(0 POR PADRAO) = TEMPO DE BLOQUEIO DO PROCESSO(INFORMADO NOS ARQUIVOS)
                if (tempoRestante > 0):
                    self.bloquear()
                else:
                    #LIBERA PROCESSO, E COLOCA UM NOVO PROCESSO NA LISTA DE PRONTOS
                    #FUNCAO APRONTAR NOVO PROCESSO, VERIFICA SE UM PROCESSO BLOQUEADO JÁ PODE FICAR PRONTO
                    #SE SIM, COLOCA NA LISTA DE PRONTOS, SE NÃO, VERIFICA NA LISTA DE TODOS OS PROCESSOS
                    self.__tempo_total_de_espera += self.execucao.waiting_time
                    self.execucao = None
                    self.aprontarNovoProcesso()

            else:
                #COMO SE PASSOU UM CICLO DO PROCESSADOR, TODOS OS PROCESSOS DA LISTA DE BLOQUEADOS SÃO DECREMENTADOS

                self.aprontarNovoProcesso()
                self.esperar()
              #  self.decrementarBloqueio()
                continue

        print(self.__total_turnarond)
        print("Tempo de Espera total: " + str(self.__tempo_total_de_espera))
        print("Tempo de Espera Média: " + str(self.__tempo_total_de_espera/101))

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

