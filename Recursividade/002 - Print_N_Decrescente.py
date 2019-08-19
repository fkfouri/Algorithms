'''
Imprimir n primeiros numeros naturais em ordem decrescente
'''

def printN(n):
    if n > 1:
        printN(n - 1)
    print(n)

#Base
printN(1)

#printN(8)