def imprimeQuadrado(numero):
    if numero <=1:
        return
    print("%d\t" %(numero*numero))

def quadrado(numero):
    return numero * numero

tamanho = 6
numQuadrado = 0

for i in range(tamanho):
    imprimeQuadrado(i)