'''
Dado um vetor ordenado de tamanho n, verificar se um determinado elementos esta ou nao presente em um vetor ordenado

Este codigo tem um bug
'''

def busca(vetor, inicio, fim, valor):
    if inicio >= fim: 
        return -1
    
    #ponto intermediario, valor inteiro
    meio_vetor = 1+ (fim + inicio)//2

    if vetor[meio_vetor] == valor:
        return meio_vetor
    
    if vetor[meio_vetor] > valor:
        return busca(vetor, inicio, meio_vetor - 1, valor)
    else:
        return busca(vetor, meio_vetor + 1, fim, valor)


vet = [ 10, 12, 18, 22, 25, 28, 32, 33, 37, 44]

print('Busca binaria de 5 =>', busca(vet, 0, len(vet) -1, 5))
print('Busca binaria de 22 =>', busca(vet, 0, len(vet) -1, 22) )
print('Busca binaria de 32 =>', busca(vet, 0, len(vet) -1, 32) )
print('Busca binaria de 43 =>', busca(vet, 0, len(vet) -1, 43) )