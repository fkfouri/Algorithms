'''
Algoritimo recursivo de Calculo Fatorial
Pode gerar problema de stackoverflow para numero muito alto

Em termos de complexidade espaco de memoria ocupa Ɵ(n), cresce desvido o uso de empilhamento.

Em termos de complexidade de tempo eh Ɵ(n), mas com fator multiplicativo alto, pois possui os custos envolvidos 
de empilhamento/desempilhamento, tornando-o mais lento que o Fatorial_Iterativo

'''

def fat(n):
    if n == 0 or n == 1:
        return 1
    return n*fat(n-1)

#Base
print('Base =>', fat(0), fat(1))

print('fatorial de 3 =>', fat(3))

print('fatorial de 6 =>', fat(6))

print('fatorial de 10 =>', fat(10))

print('fatorial de 50 =>', fat(50))