'''
Algoritimo iterativo  de Calculo Fatorial
Nao gera stakoverflow devido consumo de pilha de memoria

Otimo em termos de complexidade espaco de memoria, portanto Ɵ(1).

Em termos de complexidade de tempo eh Ɵ(n), mas o fator multiplicativo desta algoritimo eh muito menor que o Recursivo, pois nao 
possui os custos envolvidos de empilhamento/desempilhamento, tornando-o mais rapido que o Fatorial_recursivo

'''

def fat(n):
    f = 1     #=> pilha explicita, variavel que mantem os valores
    while n>0:
        f *= n
        n -= 1
    
    return f

#Base
print('Base =>', fat(0), fat(1))

print('fatorial de 3 =>', fat(3))

print('fatorial de 6 =>', fat(6))

print('fatorial de 10 =>', fat(10))

print('fatorial de 50 =>', fat(50))