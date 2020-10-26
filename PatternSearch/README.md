# Busca Padrao

Algoritimos de busca de padrões em vetores. Geralmente são algorítimos bem intricados.
- Knuth-Morris-Pratt (KMP)
- Boyer-Mooere
- Karp-Rabin

Exemplos de padrões: 
- Textos (ASCII, Unicode)
- programas
- paginas web
- DNA {A, C, G, T}

**T** -> Texto -> tamanho **n**

**P** -> Palavra -> tamanho **m**

Busca de ocorrencias de **P** em **T**, para iso se supõe-se que **n > m**.

## Prefixo e Sufixo

Padrão **P** é representado como **P[0..m-1]**.

Prefixo -> **Pi = P[0..i]**
Sufixo -> **Si = P[i..m-1]**