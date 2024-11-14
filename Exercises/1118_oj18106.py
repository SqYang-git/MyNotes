def rotmatrix(n):
    if n == 1:
        return [[1]]
    buffer = rotmatrix(n - 1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[0][i] = i + 1
    for i in range(1, n):
        result[i][n - 1] = n + i
    for i in range(1, n):
        for j in range(n - 1):
            result[i][j] = buffer[n - 1 - i][n - 2 - j] + 2 * n - 1
    return result


n = int(input())
matrix = rotmatrix(n)
for row in matrix:
    print(' '.join(map(str, row)))
