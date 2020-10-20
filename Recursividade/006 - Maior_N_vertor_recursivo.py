
'''
Algoritimo recursivo para encontrar o maior valor de um vetor.
Tradicionalmente se usa o modelo iterativo (for) 
'''
vet = [ 1, 2, 3, 4, 5, 9, 8, 7, 6, 5]

def max(n):
    if n == 1:
        return vet[0]

    m = max(n - 1)

    if m > vet[n -1]:
        return m
    else:
        return vet[n-1]


print('O maior valor do vetor eh:', max( len(vet) ))


