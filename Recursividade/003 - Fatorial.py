'''
Algoritimo recursivo de Calculo Fatorial

'''

def fat(n):
    if n == 0 or n == 1:
        return 1
    return n*fat(n-1)

#Base
#print(fat(0), fat(1))

#print(fat(3), fat(6))

print(fat(50))