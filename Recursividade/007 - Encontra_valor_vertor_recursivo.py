
'''
Algoritimo recursivo para encontrar se um valor esta no vetor.
A saída é boleana.
'''


def esta_no_vetor(vetor, tamanho_vetor, valor):
    if tamanho_vetor == 1:
        return valor == vetor[0]
    
    b = esta_no_vetor(vetor, tamanho_vetor - 1, valor)

    return b or valor == vetor[tamanho_vetor - 1]

vet = [ 1, 2, 3, 4, 5, 9, 8, 7, 6, 5]

print('O nº 4 esta no vetor?', esta_no_vetor(vet, len(vet), 4) )
print('O nº 5 esta no vetor?', esta_no_vetor(vet, len(vet), 5) )
print('O nº 12 esta no vetor?', esta_no_vetor(vet, len(vet), 12) )


