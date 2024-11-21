dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# dfs用于把所有相连的1变成0
def dfs(x, y):
    global matrix
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if matrix[nx][ny] == 1:
            matrix[nx][ny] = 0
            dfs(nx, ny)
    return


count = 0  # 初始化计数
n, m = map(int, input().split())
matrix = [[0 for i in range(m+2)]]  # 加保护圈
for i in range(n):
    matrix.append([0] + list(map(int, input().split())) + [0])
matrix.append([0 for i in range(m+2)])

for i in range(1, n+1):
    for j in range(1, m+1):
        # 对可搜索到的1
        if matrix[i][j] == 1:
            count += 1  # 记录一个区块
            matrix[i][j] = 0  # 将碰到的点标记为0
            dfs(i, j)  # 将周围区块的点标记为0
print(count)
