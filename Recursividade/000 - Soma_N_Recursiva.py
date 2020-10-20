'''
Algoritimo iterativo de Soma de numeros naturais N para n > 0 

Em termos de complexidade espaco ocupa Ɵ(n), cresce desvido o uso de empilhamento.

Em termos de complexidade de tempo eh Ɵ(n), fator multiplicativo alto em comparacao com o Iterativo, portanto, mais lento.
'''
def soma(n):
    if (n == 1):
        return 1
    return n + soma(n - 1)

#Base
print('Base =>', soma(1))

print('soma de 3 =>', soma(3))

print('soma de 6 =>', soma(6))

print('soma de 10 =>', soma(10))

print('soma de 50 =>', soma(50))