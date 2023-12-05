n = int(input('Enter matrix size: '))
matrix = []
for i in range(n):
    row = list(map(int, input("enter numbers: ").split(', ')))
    matrix.append(row)

diagonal_sum = 0
for i in range(n):
    for j in range(i + 1):
        diagonal_sum += matrix[i][j]


print(diagonal_sum)