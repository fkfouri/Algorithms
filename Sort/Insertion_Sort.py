'''
Este codigo executa a ordenacao por insercao. solucao analogo ao ordenacao de cartas.
'''
def Insert_Sort(A):
    mySize = len(A)
    for j  in range(1, mySize): #mudanca de 2 para 1, pois a indexacao no python comeca por zero
        key_compare_B = A[j]
        i = j - 1
        key_compare_A = A[i]
        while i>= 0 and A[i] > key_compare_B: #inclusao do >= 0 pois a indexacao no python comeca por zero
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key_compare_B
    return A

col = [5,2,4,6,1,3]
col2 = Insert_Sort(col)
print(col2)