dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
maxVal = float('-inf')
best_path = []


def dfs(maze, x, y, nowVal, path):
    global maxVal, best_path
    # 如果到达终点，我们需要检查是否是最大的权值路径
    if x == n and y == m:
        if nowVal > maxVal:
            maxVal = nowVal
            best_path = path.copy()
        return
    # 尝试移动到四个方向
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 确保新的位置在边界内且没有被访问过
        if 1 <= nx <= n and 1 <= ny <= m and maze[nx][ny] != -10000:
            buffer = maze[nx][ny]
            maze[nx][ny] = -10000  # 标记为访问过
            dfs(maze, nx, ny, nowVal + buffer, path + [(nx, ny)])
            maze[nx][ny] = buffer  # 恢复原值


# 输入棋盘大小
n, m = map(int, input().split())
# 初始化迷宫，并在边缘加上障碍
maze = [[-10000 for j in range(m + 2)]]
for i in range(n):
    maze.append([-10000] + list(map(int, input().split())) + [-10000])
maze.append([-10000 for j in range(m + 2)])
maze[1][1] = -10000  # 标记起点为访问过以防止返回

dfs(maze, 1, 1, maze[1][1], [(1, 1)])

# 输出路径
for coord in best_path:
    print(f"{coord[0]} {coord[1]}")
