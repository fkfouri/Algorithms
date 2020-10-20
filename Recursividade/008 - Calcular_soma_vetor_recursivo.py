
'''
Algoritimo recursivo calcular a soma do vetor
'''

def soma(vetor, tamanho_vetor):
    if tamanho_vetor == 1:
        return vetor[0]

    return soma(vetor, tamanho_vetor - 1) + vetor[tamanho_vetor -1]


vet = [ 1, 2, 3, 4]

print('A soma dos elementos do vetor resulta:', soma(vet, len(vet) ))


