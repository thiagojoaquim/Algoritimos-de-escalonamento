
from processo import Processos

def carregar(caminho):
    file = open(caminho)
    cenario = file.read()
    cenario = cenario.split("\n")
    processos = []
    for c in cenario:
        c = c.split(',')
        if c != ['']:
            aux = Processos.Processos(c[0], c[1], c[2], c[3], c[4])
            processos.append(aux)
    file.close()
    return processos

def escrever(string):
    file = open("../Arquivos/Saida.txt",'w')
    file.write(string)
    file.close()