# 행렬의 곱셈문제
# 두 n * x 행렬의 곱을 구하시오 

# 선형 대수

# A = [a11, a12]   B = [b11, b12]
#     [a21, a22]       [b21, b22]

# [2, 3] * [5, 7] = [28, 38]
# [4, 1]   [6, 8]   [26, 36]

# 3중 for 문

def matrixmult (A, B):
    n = len(A)
    C = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
print('A=', A)
print('B=', B)
C = matrixmult(A, B)
print('C=', C)
