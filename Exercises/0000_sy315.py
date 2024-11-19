dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maxVal = float('-inf')
def dfs(maze, x, y, nowVal):
    global maxVal
    if x == n and y == m:
        if nowVal > maxVal:
            maxVal = nowVal
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] != -10000:
            buffer = maze[x][y]
            maze[x][y] = -10000
            nextVal = nowVal + maze[nx][ny]
            dfs(maze, nx, ny, nextVal)
            maze[x][y] = buffer


n, m = map(int, input().split())
maze = [[-10000 for j in range(m+2)]]
for i in range(n):
    maze.append([-10000] + list(map(int, input().split())) + [-10000])
maze.append([-10000 for j in range(m+2)])

dfs(maze, 1, 1, maze[1][1])
print(maxVal)
