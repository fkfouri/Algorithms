


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # create temp arrays 
    L = [0] * (n1)  #Left
    R = [0] * (n2)  #Right

    for i in  range(0 , n1):
        L[i] = A[p + i] #indexacao no python comeca por zero
    for j in  range(0 , n2):
        R[j] = A[q + 1 + j] #indexacao no python comeca por zero

    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = p     # Initial index of merged subarray 

    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        A[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        A[k] = R[j] 
        j += 1
        k += 1



def mergeSort(A, p, r):
    if p < r:

        q = (p+(r-1))//2

        # Sort first and second halves 
        mergeSort(A, p, q) 
        mergeSort(A, q + 1, r) 
        merge(A, p, q, r)         


col = [ 12, 4, 13, 5, 7, 11 ,8]
print(col)
mergeSort(col, 0, len(col) - 1)
print(col)