n, m1, m2 = map(int, input().split())
matrix1 = [[0] * n for _ in range(n)]
matrix2 = [[0] * n for _ in range(n)]
for i in range(m1):
    x, y, m1 = map(int, input().split())
    matrix1[x][y] = m1
for i in range(m2):
    x, y, m2 = map(int, input().split())
    matrix2[x][y] = m2
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
for i in range(n):
    for j in range(n):
        if result[i][j] != 0:
            print(f"{i} {j} {result[i][j]}")
