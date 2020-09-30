'''
Algoritimo intrativo  de Calculo Fatorial
Nao gera stakoverflow devido consumo de pilha de memoria

'''

def fat(n):
    f = 1
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