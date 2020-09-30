# T(n) = 8T(N/2) +cn^2    => O(n^3)
# 
# 8 multiplicacoes e 4 adicoes
# 

def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print ("Cannot multiply the two matrices. Incorrect dimensions.")
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print (C)

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C




a = [[1,2],[3,4]]
b = [[5,6],[7,8]]

print(matrixmult(a,b))