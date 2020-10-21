'''
Algoritimo que implementa uma fila (QUEUE) usando vetor. FIFO (First In, First Out)
Funcoes size, isEmpty, first, dequeue e enqueue.

O Vetor eh usado de forma circular, para não gatar tempo de deslocamento.

Todas as operações são executadas em tempo constante Ɵ(1).

Se fosse implementar uma busca na pilha seria ineficiente pois o tempo de pior caso seria Ɵ(N),
ou seja, o tamanho do vetor.
'''

# tamanho da pilha
N = 5
# vetor Q
Q = [None] * N
# onde f eh o primeiro que entrou na fila e r o ultimo que entrou.
# f igual a r representa fila vazia.
f = -1
r = -1

def size():
    return (N -f +r) % N

def isEmpty():
    return f == r

def first():
    if isEmpty():
        return 'Error'
    return Q[f]

def dequeue():
    global Q, f
    if isEmpty():
        return 'Error'

    out = Q[f]  
    Q[f] = None
    f = (f+1)  % N
    return out

def enqueue(x):
    global Q, r
    if size() == N -1:
        return 'Error'

    Q[r] = x
    r = (r + 1) % N
    

print('Tamanho:' , size())
print('dequeue:', dequeue())
print('Esta vazio?', isEmpty())

enqueue(1)
print('Tamanho:' , size())
print('first:', first())
print('Esta vazio?', isEmpty())

enqueue(2)
print('Tamanho:' , size())
print('first:', first())
print('Esta vazio?', isEmpty())

enqueue(3)
print('Tamanho:' , size())
print('dequeue:', dequeue())
print('first:', first())
print('Esta vazio?', isEmpty())


enqueue(4)
enqueue(5)
enqueue(6)
enqueue(7)
enqueue(8)
print('Tamanho:' , size())

print('dequeue:', dequeue())
print('dequeue:', dequeue())
print('dequeue:', dequeue())
print('dequeue:', dequeue())
enqueue(6)
enqueue(7)
enqueue(8)
print('dequeue:', dequeue())
print('dequeue:', dequeue())
print('dequeue:', dequeue())
print('dequeue:', dequeue())