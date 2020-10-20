'''
Imprimir n primeiros numeros naturais em ordem decrescente
'''

def printN(n):
    print(n)
    if n > 1:
        printN(n - 1)
    

#Base
#printN(1)


printN(8)