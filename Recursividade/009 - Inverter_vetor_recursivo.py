
'''
Algoritimo recursivo que inverte os valores de um vetor
'''

def invert(vetor, inicio, fim):
    if fim > inicio:
        aux = vetor[fim]
        vetor[fim] = vetor[inicio]
        vetor[inicio] = aux

        invert(vetor, inicio + 1, fim - 1)

vet = [ 1, 2, 3, 4, 5, 6]

invert(vet, 0, len(vet) - 1 )

print('Inverte o vetor:', vet)


