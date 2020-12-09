# Arvore


# Percursos em arvore

É uma sequencia em que cada um dos nós da árvore aparece exatamente uma vez (não precisa estar necessariamente unidos por arestas).

Um árvore com N nós possui N! percursos diferentes.

Há o **percurso em largura** (extensão) e **percurso em profundidade**.

## Percurso em largura

Começa na raiz e passa ordenadamente por todos os níveis subsequentes, visitando-se primeir os nós da esquerda para a direita.

Esta implementação usa a **fila**. Depois que um nó é visitado, seus filhos são colocados no final dessa fila. O próximo nó a ser visitado é o que esta no início da fila. 

## Percurso em profundidade

Prossegue tanto quanto possível à esquerda (ou à direita). Em seguida volta ao último nó visitado e recomeça. O processo se repete até que todos sejam visitados.

Pode ser implementado recursivamente ou com uma pilha explicita.

- Pre-order: Raiz, Esquerda, Direita
- In-order: Esquerda, Raiz, Direira
- Pos-order: Esquerda, Direita, Raiz

