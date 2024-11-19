# 移动方式记录
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 定义dfs函数
def dfs(maze, x, y):
    # 引入全局计数变量
    global count
    # 尝试四个方向移动
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 如果可以到达终点,则计数加1并继续搜索
        if maze[nx][ny] == "end":
            count += 1
            continue
        # 如果未碰到障碍物或达到终点
        if maze[nx][ny] == 0:
            # 将当前位置标记为不可返回,防止重复搜索
            maze[x][y] = 2
            # 继续调用dfs函数搜索
            dfs(maze, nx, ny)
            # 回溯,将当前位置标记为可返回
            maze[x][y] = 0
    # 形式上返回,无返回值,但会修改全局变量count
    return


n, m = map(int, input().split())
maze = [[-1 for i in range(m+2)]]
for i in range(n):
    maze.append([-1] + list(map(int, input().split())) + [-1])
maze.append([-1 for i in range(m+2)])
# 输入迷宫信息,并加保护圈

maze[1][1] = "start"  # 起点标为非0值,防止被搜索到
maze[n][m] = "end"

count = 0
# 从start开始进行深度优先搜索
dfs(maze, 1, 1)
print(count)
