'''
Este codigo executa a ordenacao por insercao. solucao analogo ao ordenacao de cartas.
Ordenacao Crescente

tempo de execuçao de pior caso he Θ(n^2)
'''
def Insert_Sort(A):
    mySize = len(A)
    for j in range(1, mySize): #mudanca de 2 para 1, pois a indexacao no python comeca por zero
        key_compare_B = A[j]
        i = j - 1
        key_compare_A = A[i]
        while i>= 0 and A[i] > key_compare_B: #inclusao do >= 0 pois a indexacao no python comeca por zero
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key_compare_B
    return A


'''
Este codigo executa a ordenacao por insercao. solucao analogo ao ordenacao de cartas.
Ordenacao Decrescente
'''
def Insert_Sort_Desc(A):
    mySize = len(A)
    for j in range(1, mySize):
        key_compare_B = A[j]
        i = j - 1
        key_compare_A = A[i]
        while i>= 0 and A[i] < key_compare_B: #para deixar em ordem descrescente, basta colocar menor A[i] < key_compare_B
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key_compare_B
    return A , "Decrescente"

col = [5,2,4,6,1,3]
print(Insert_Sort(col))

col = [31,41,59,26,41,58]           #EXO 2.1 - 1
print(Insert_Sort(col))

col = [5,2,4,6,1,3]                 #EXO 2.2 - 2
print(Insert_Sort_Desc(col))