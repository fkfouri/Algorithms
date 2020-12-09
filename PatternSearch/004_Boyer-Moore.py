

def printComparacoes(numero, text):
    print('\n'+ str(numero), 'é o numero de comparacoes em:', '"' + text +'"')

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


def BoyerMooreMatch(T, P):

    L = UltimaOcorrencia(P)

    m = len(P)
    n = len(T)
    i = m-1
    j = m-1

    comparacoes = 0

    while True:
        comparacoes+=1
        if T[i] == P[j]:
            if j == 0:
                printComparacoes(comparacoes, T)
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
    
    printComparacoes(comparacoes, T)
    return -1



texto = "This is a simple text for a test."
palavra = "text"
print(BoyerMooreMatch(texto, palavra))

texto = "a pattern matching algorithm"
palavra = "rithm"
print(BoyerMooreMatch(texto, palavra))


texto = "abacaabadcabacabaabb"
palavra = "abacab"
print(BoyerMooreMatch(texto, palavra))


texto = "a jabuticaba acabou de acabar"
palavra = "cabar"
print(BoyerMooreMatch(texto, palavra))


texto = "vi na mata uma arara e duas aranhas"
palavra = "araras"
print(BoyerMooreMatch(texto, palavra))

texto = "faturei com folga na prova de complexidade de algoritimo"
palavra = "algo"
print(BoyerMooreMatch(texto, palavra))

texto = "esta prova e mais longa que complicada"
palavra = "cada"
print(BoyerMooreMatch(texto, palavra))