# G4 solved

A, B = map(int, input().split())
matrix = []

for i in range(A):
    row = list(map(int, input().split()))
    matrix.append(row)

def multiply(to_mul_matrix, do_mul_matrix):
    result = [[0 for _ in range(A)] for _ in range(A)]
    for result_col in range(A):
        for result_row in range(A):
            temp = 0
            for i in range(A):
                result[result_col][result_row] += to_mul_matrix[result_col][i] * do_mul_matrix[i][result_row] % 1000
    return result

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val % 1000, end=' ')
        print()

def mul_B_time(B):
    if B == 1:
        return matrix
    else:
        temp = mul_B_time(B // 2)
        if B % 2 == 0:
            return multiply(temp, temp)
        else:
            return multiply(multiply(temp, temp), matrix)

print_matrix(mul_B_time(B))