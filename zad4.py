n = int(input("enter matrix size: "))
matrix = []
for i in range(n):
    row = list(map(int, input("enter numbers: ").split(', ')))
    matrix.append(row)
diagonal_sum = sum(matrix[g][g] for g in range(n))
print("sum is", diagonal_sum)
