n = int(input('Enter matrix size: '))
matrix = []
for i in range(n):
    row = list(map(int, input("enter numbers: ").split(', ')))
    matrix.append(row)
diagonal_sum = sum(matrix[g][n-1-g] for g in range(n))
print("sum is", diagonal_sum)

print(matrix)