#
# complexidade O(n.m), ou seja, 
# no pior caso, todos os caracteres de P serao comparados com todos os caracteres de T
#  
# 
# 
def bruteForceMatch(P, T):
    n = len(P)
    m = len(T)
    if m > n:
        return "Error size"

    for i in range(n):
        j = 0
        if T[j]==P[i+j]:
            while j<m and T[i+j]==P[j]:
                j+=1
            if j==m:
                return i
    
    return -1


phase = "This is a simple text for a test."
word = "text"

print(bruteForceMatch(phase, word))