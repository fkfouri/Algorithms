# Written by Magnus Lie Hetland
def partition(v, left, right):
    pivot = v[left]
    l = left + 1
    r = right
    while True:
        while(l < right and v[l] < pivot):
            l+=1
        while(r > left and v[r] >= pivot):
            r-=1

        if l>=r:
            break

        aux = v[l]
        v[l] = v[r]
        v[r] = aux       

    v[left] = v[r]
    v[r]=pivot
    return r

def quicksort(list, start, end):
    if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split - 1)
        quicksort(list, split + 1, end)
    else:
        return

# 
# Algoritimo modificado para evitar a pilha de execucao
#
def quicksort2(list, start, end):
    while start < end:
        p = partition(list, start, end)
        if (p - start < end - p):
            quicksort2 (list, start, p - 1)
            start = p + 1
        else:
            quicksort2(list, p+1, end)
            end = p -1
        


list = [2,3,6,10,5,3,4]
start = 0
end = len(list)-1
quicksort(list,start,end)
print (' '.join(map(str,list)))

list = [2,3,6,10,5,3,4]
start = 0
end = len(list)-1
quicksort2(list,start,end)
print (' '.join(map(str,list)))