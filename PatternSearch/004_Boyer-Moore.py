



###
# A funcao Falha gasta o tempo de Ɵ(m)
#
def UltimaOcorrencia(P):
    
    z = 256                     # tamanho do alfabeto ASCII
    m = len(P)

    L = [None] * z              
    for k in range(z):
        L[k] = -1
    
    for k in range(m):
        c = ord(P[k])
        L[c] = k
    
    return L


def BoyerMooreMathc(T, P):

    L = UltimaOcorrencia(P)

    m = len(P)
    n = len(T)
    i = m-1
    j = m-1

    while True:
        if T[i] == P[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            c = ord(T[i])
            x = L[c]
            i += m - min(j, 1 + x)          # trecho do algoritimo que faz os 3 casos do Boyer-Moore
            j = m - 1

        if i > n - 1:
            break
    
    return -1



texto = "This is a simple text for a test."
palavra = "text"


print(BoyerMooreMathc(texto, palavra))