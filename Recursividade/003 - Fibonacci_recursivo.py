'''
Algoritimo iterativo de Calculo Fibonacci

Otimo em termos de complexidade espaco de memoria, portanto Ɵ(1).

Em termos de complexidade de tempo eh Ω(2^(n/2)), ou seja, cresce na ordem exponencial de n. Esse foi um piso calculado, mas
ja demonstra a alta complexidade de tempo de um Fibonacci recursivo.

Melhor usar o Fibonacci Iterativo.

'''

def fib(n):
    if( n == 0 or n == 1):
        return 1
    return fib(n-1) + fib(n-2)



    #Base
print('Base =>', fib(0), fib(1))
print('Fibonacci de 3 =>', fib(3))
print('Fibonacci de 6 =>', fib(6))
print('Fibonacci de 10 =>', fib(10))
print('Fibonacci de 30 =>', fib(30))
print('Fibonacci de 50 =>', 'Nao processa')