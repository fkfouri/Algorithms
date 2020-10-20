'''
Algoritimo iterativo de Soma de numeros naturais N para n > 0 

Otimo em termos de complexidade espaco de memoria, portanto Ɵ(1).

Em termos de complexidade de tempo eh Ɵ(n), fator multiplicativo baixo em comparacao com o Recursivo, portanto, mais rapido.
'''

def soma(n):
    s = n
    while n > 1:
        n -= 1
        s += n
    return s

#Base
print('Base =>', soma(1))

print('soma de 3 =>', soma(3))

print('soma de 6 =>', soma(6))

print('soma de 10 =>', soma(10))

print('soma de 50 =>', soma(50))