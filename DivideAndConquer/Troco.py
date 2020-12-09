

#Por divisao e conquista
def DCMakeChange(moedas, troco):
    if (troco == 0):
        return 0
    
    q = troco   #solucao obvia com somente moedas de 1 centavo

    for i in range(len(moedas)):
        if moedas[i] > troco:
            break
        q = min(q, 1 + DCMakeChange(moedas, troco - moedas[i]))

    return q



moedas = [1, 10, 25, 50]
troco = 30

print(DCMakeChange(moedas, troco))