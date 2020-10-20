'''
Representacao binaria de um numero natural
'''

def decToBin(n):
    if n==0: return ''
    else:
        return decToBin(n//2) + str(n%2)

pilha = []
def decToBinWithStack(n):  
    while n//2 >1:
        pilha.append(n%2)
        n = n//2
    pilha.append(n%2)
    pilha.append(n//2)

    out = ''
    while pilha:
        out += str(pilha.pop())

    return out


#base
#print(decToBin(1))

ref = 44

print(decToBin(ref))


#print(ref//2, ref%2)


print(decToBinWithStack(ref))
