'''
Representacao binaria de um numero natural
'''

def decToBin(n):
    if n==0: return ''
    else:
        return decToBin(n//2) + str(n%2)

#base
#print(decToBin(1))

print(decToBin(35))