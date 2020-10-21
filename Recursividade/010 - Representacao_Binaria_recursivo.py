'''
Representacao binaria de um numero natural algoritimo recursivo
'''

def bin(n):
    if n==0: return str(0)
    else:
        return bin(n//2) + str(n%2)

print('Base =>', bin(0))
print('Binario de 3 =>', bin(3))
print('Binario de 6 =>', bin(6))
print('Binario de 43 =>', bin(43))