
def strassen_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    def add(X, Y):
        return [[X[i][j] + Y[i][j] for j in range(len(X))]
                for i in range(len(X))]

    def sub(X, Y):
        return [[X[i][j] - Y[i][j] for j in range(len(X))]
                for i in range(len(X))]

    M1 = strassen_multiply(add(A11, A22), add(B11, B22))
    M2 = strassen_multiply(add(A21, A22), B11)
    M3 = strassen_multiply(A11, sub(B12, B22))
    M4 = strassen_multiply(A22, sub(B21, B11))
    M5 = strassen_multiply(add(A11, A12), B22)
    M6 = strassen_multiply(sub(A21, A11), add(B11, B12))
    M7 = strassen_multiply(sub(A12, A22), add(B21, B22))

    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


n = int(input("Enter the order of matrices: "))

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

size = 1
while size < n:
    size *= 2

A += [[0] * n for _ in range(size - n)]
B += [[0] * n for _ in range(size - n)]

A = [row + [0] * (size - n) for row in A]
B = [row + [0] * (size - n) for row in B]

C = strassen_multiply(A, B)

print("Product Matrix:")
for row in C[:n]:
    print(*row[:n])
