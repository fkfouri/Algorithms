#
# Complexidade exata é O((n-m).m) = O(n.m), ou seja,
# no tempo de pior caso, todos os caracteres de P serao comparados com todos os caracteres de T.
# O que na pratica eh muito ruin, pois é uma multiplicação de n e m.  
def bruteForceMatch(T, P):
    
    m = len(P)
    n = len(T)

    if m > n:
        return "Error size"

    for i in range(n-m):
        j = 0
        #if T[j]==P[i+j]:
        while j<m and T[i+j]==P[j]:
            j += 1
        if j==m:
            return i        # P encontrado em T[i]
    
    return -1               # P nao encontrado


texto = "This is a simple text for a test."
palavra = "text"

print(bruteForceMatch(texto, palavra))