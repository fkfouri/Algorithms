

def printComparacoes(numero, text):
    print('\n'+ str(numero), 'é o numero de comparacoes em:', '"' + text +'"')

###
# A funcao Falha gasta o tempo de Ɵ(m)
#
def FailureFunction(P):
    
    j = 0                       # indice que percorre os prefixos
    i = 1                      # indice que percorre os sufixos
    m = len(P)

    F = [None] * m
    F[0] = 0

    while i < m:
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
    F = FailureFunction(P)              #gasta tempo Ɵ(m)

    i = 0
    j = 0
    m = len(P)
    n = len(T)

    comparacoes = 0

    while (i < n):
        comparacoes +=1
        if (T[i] == P[j]):
            if j == m-1:
                printComparacoes(comparacoes, T)
                return i - j
            else:
                i += 1
                j += 1
        else:
            if j != 0:
                j = F[j-1]
            else:
                i += 1
    
    printComparacoes(comparacoes, T)
    return -1



texto = "This is a simple text for a test."
palavra = "text"
print(KMPMatch(texto, palavra))

texto = "vi na mata uma arara e duas aranhas"
palavra = "araras"
print(KMPMatch(texto, palavra))


texto = "faturei com folga na prova de complexidade de algoritmo"
palavra = "algo"
print(KMPMatch(texto, palavra))


texto = "abacaabaccabacabaabb"
palavra = "abacab"
print(KMPMatch(texto, palavra))


texto = "a jabuticaba acabou de acabar"
palavra = "cabar"
print(KMPMatch(texto, palavra))


texto = "esta prova e mais longa que complicada"
palavra = "cada"
print(KMPMatch(texto, palavra))

texto = "vi na mata uma arara e duas aranhas"
palavra = "arara"
print(KMPMatch(texto, palavra))

texto = "doce de batata doce"
palavra = "doce"
print(KMPMatch(texto, palavra))