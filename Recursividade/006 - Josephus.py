'''
Josephus Problem é um desafio de descobrir quem no grupo continuara vivo.
A ideia é que em uma disposicao em sentido horario, o soldado mata o proximo, 
e o seguinte mata o proximo e assim sucessivamente ate sobrar um unico soldado. 
'''

ls = [1,2,3,4,5]

def josephusFK(ls, skip = 1):
    i = 0
    if ls.count == 1:
        return ls(0)

    for s in (ls):
        i += 1
        if i >= skip + 1:
            ls.remove(s)
            break
    
    return josephusFK(ls, skip)
    

#print(josephusFK(ls))


def josephus(n, k): 
  
      if (n == 1): 
          return 1
      else: 
      
      
          # The position returned by  
          # josephus(n - 1, k) is adjusted 
          # because the recursive call 
          # josephus(n - 1, k) considers 
          # the original position  
          # k%n + 1 as position 1  
          return (josephus(n - 1, k) + k-1) % n + 1
  
# Driver Program to test above function 
  
n = 5
k = 2
  
print("The chosen place is", josephus(n, k))    


