'''
Representacao binaria de um numero natural algoritimo iterativo com pilha
'''

pilha = []
def decToBinWithStack(n):  
    while n//2 >1:
        pilha.append(n%2)
        n = n//2
    pilha.append(n%2)
    pilha.append(n//2)

    out = ''
    while pilha:
        out += str(pilha.pop())

    return out


print('Base =>', decToBinWithStack(0))
print('Binario de 3 =>', decToBinWithStack(3))
print('Binario de 6 =>', decToBinWithStack(6))
print('Binario de 43 =>', decToBinWithStack(43))


