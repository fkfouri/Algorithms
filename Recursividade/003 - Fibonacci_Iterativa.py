'''
Algoritimo iterativo de Calculo Fibonacci

Otimo em termos de complexidade espaco de memoria, portanto Ɵ(1).

Em termos de complexidade de tempo linera Ɵ(n), com fator multiplicativo baixo

Muito melhor em complexidade de tempo e espaço que o Fibonacci_recursivo
'''

def fib(n):
    if( n == 0 or n == 1):
        return 1
    f1, f2, f3 = 1, 1, None
    
    for i in range(2, n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    return f3


print('Base =>', fib(0), fib(1))
print('Fibonacci de 3 =>', fib(3))
print('Fibonacci de 6 =>', fib(6))
print('Fibonacci de 10 =>', fib(10))
print('Fibonacci de 30 =>', fib(30))
print('Fibonacci de 50 =>', fib(50))