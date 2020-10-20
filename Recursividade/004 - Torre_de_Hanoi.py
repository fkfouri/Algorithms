'''
Algoritimo Recursivo de Torres de Hanoi - mover discos de uma torre para outra num total, utilizando uma torre auxiliar, sem nunca
colocar um disco maior em cima de um disco menor.

Na resolução deste problema o uso de Recursividade é muito melhor do que o Iterativo.

Em termos de complexidade de tempo eh Ɵ(2^n).
'''

#n => numero de discos
#org => torre de origem
#dest => torre de destino
#aux => torre auxiliar
def hanoi(n, org, dest, aux):
    if (n == 1):
        print('Move de', org, 'para', dest)
    else:
        hanoi(n-1, org, aux, dest)
        print('Move de', org, 'para', dest)
        hanoi(n-1, aux, dest, org)

hanoi(3, "A", "B", "C")
print(20*'=')
hanoi(4, "A", "B", "C")

