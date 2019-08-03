
from processo import Processos

def carregar():
    file = open("../Arquivos/cenario1.txt")
    cenario = file.read()
    cenario = cenario.split("\n")
    print(cenario)
    cenario = cenario[0:1]
    processos = []
    for c in cenario:
        c = c.split(',')
        if c != ['']:
            aux = Processos.Processos(c[0], c[1], c[2], c[3], c[4])
            processos.append(aux)
    return processos
