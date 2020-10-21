'''
Gray Code
Algoritimo recursivo que fara todas as representações de bits, onde a modificacao
entre as formas mudem apenas um bit.

Nao é trivial encontrar o resultado usando algoritimo iterativo.

Ex 2 bit
00
01
11
10

Ex 3 bit - Observe que de uma representacao para outra so mudou 1 bit por vez. Nao acontece 000 ir para 011.
000
001
011
010
110
111
101
100

n = 1                                 0       e       1

n = 2                         0       1       -       1       0           => observe que tem copiou a resposta do n1 e invertido
                             00      01              11      10

n = 3        00      01      11      10      -       10      11      01      00
            000     001     011     010     -       110     111     101     100     => na primeira metade insere 0, na segunda 1
'''



def gray_code(n):
    if n <= 0:
        return []
    if n == 1:
        return ['0', '1']

    res = gray_code(n - 1)
    #       metade                  metade invertida
    return ['0' + s for s in res] + ['1' + s for s in res[::-1]]

print(gray_code(4))