'''
Imprimir n primeiros numeros naturais em ordem crescente
'''

def printN(n):
    if n > 1:
        printN(n - 1)
    print(n)

#Base
printN(10)

#printN(8)