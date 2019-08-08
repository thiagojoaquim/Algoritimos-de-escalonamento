from algoritmos import RR
from algoritmos import Escalonamento
from algoritmos import MultilevelFeedback
from algoritmos import Escalonamento_por_prioridade
from algoritmos import Escalonamento_garantido
from algoritmos import StateDependent
from algoritmos import HRRN
from algoritmos import Escalonamento_por_loteria
from utilitarios import Util

if __name__ == '__main__':
    a = input("digite o numero do cenario(1,2,3,4 ou 5)")
    caminho = "../Arquivos/cenario" + str(a) + ".txt"
    print("Selecione o algoritmo de escalonamento")
    print("1 para Priority Scheduling")
    print("2 para Lottery Scheduling")
    print("3 para HRRN Scheduling")
    print("4 para State Dependent Scheduling")
    print("5 para RR Scheduling")
    print("6 para Garanted Scheduling")
    print("7 para MultilevelFeedback Scheduling")
    algoritmo = int(input())
    escalonamento = None
    if algoritmo == 1:
        escalonamento = Escalonamento_por_prioridade.Prioridade(100, Util.carregar(caminho), 1)
    elif algoritmo == 2:
        escalonamento = Escalonamento_por_loteria.Loteria(100, Util.carregar(caminho), 1)
    elif algoritmo == 3:
        escalonamento = HRRN.HRRN(100, Util.carregar(caminho), 1)

    elif algoritmo == 4:
        escalonamento = StateDependent.StateDependent(100, Util.carregar(caminho), 4)
    elif algoritmo == 5:
        escalonamento = RR.RR(100, Util.carregar(caminho), 4)
    elif algoritmo == 6:
        escalonamento = Escalonamento_garantido.Garantido(100, Util.carregar(caminho), 1)
    elif algoritmo == 7:
        escalonamento = MultilevelFeedback.MultilevelFeedback(100, Util.carregar(caminho), 1,2,
                                                              4)
    else :
        print("Input Inválido")

    if algoritmo == int(5):
        escalonamento.executar(None)
    else:
        escalonamento.executar()





