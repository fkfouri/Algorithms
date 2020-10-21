'''
Algoritimo que implementa uma pilha (stack) usando vetor LIFO (Last In, First Out).
Funcoes Size, isEmpty, top, push e pop

Todas as operações são executadas em tempo constante Ɵ(1).

Se fosse implementar uma busca na pilha seria ineficiente pois o tempo de pior caso seria Ɵ(N),
ou seja, o tamanho do vetor.
'''

# tamanho da pilha
N = 10
# vetor S
S = [None] * N
# quantidade de elementos
t = -1


def size():
    return t + 1

def isEmpty():
    return t < 0

def top():
    if isEmpty():
        return 'Error'
    return S[t]

def push(x):
    global t, S
    if size() == N:
        return 'Error'
    t += 1
    S[t] = x

def pop():
    global t, S
    if isEmpty():
        return 'Error'
    out = S[t]
    t -=1
    return out


print('Tamanho:' , size())
print('Pop:', pop())
print('Esta vazio?', isEmpty())

push(1)
print('Tamanho:' , size())
print('Top:', top())
print('Esta vazio?', isEmpty())

push(4)
print('Tamanho:' , size())
print('Top:', top())
print('Esta vazio?', isEmpty())

push(1)
print('Tamanho:' , size())
print('Pop:', pop())
print('Esta vazio?', isEmpty())