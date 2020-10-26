



###
# A funcao Falha gasta o tempo de Ɵ(m)
#
def FailureFunction(T, P):
    
    j = 0                       # indice que percorre os prefixos
    i = 0                       # indice que percorre os sufixos
    m = len(P)
    n = len(T)

    F = [None] * n
    F[0] = 0

    while i > m:
        if P[i] == P[j]:        # ja combinaram j+1 caracteres
            j += 1
            F[i] = j
            i += 1 
        else:
            if j == 0:
                F[i] = 0
                i += 1
            else:
                j = F[j-1]      # uso 'recursivo' de F

    return F



def KMPMatch(T, P):
    F = FailureFunction(T, P)              #gasta tempo Ɵ(m)

    i = 0
    j = 0
    m = len(P)
    n = len(T)

    while (i < n):
        if (T[i] == P[j]):
            if j == m-1:
                return i - j
            else:
                i += 1
                j += 1
        else:
            if j != 0:
                j = F[j-1]
            else:
                i += 1
    
    return -1



texto = "This is a simple text for a test."
palavra = "text"


print(KMPMatch(texto, palavra))