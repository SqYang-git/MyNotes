dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

canReach = False
def dfs(x, y, maze, steps):
    global canReach
    if canReach:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == "end":
            if steps == k-1:
                canReach = True
                return
            continue
        if maze[nx][ny] == 0:
            if steps < k-1:
                maze[x][y] = 2
                dfs(nx, ny, maze, steps+1)
                maze[x][y] = 0


n, m, k = map(int, input().split())
maze= [[-1 for i in range(m+2)]]
for i in range(n):
    maze.append([-1]+list(map(int, input().split()))+[-1])
maze.append([-1 for i in range(m+2)])

maze[1][1] = "start"; maze[n][m] = "end"
dfs(1, 1, maze, 0)
print("Yes" if canReach else "No")
