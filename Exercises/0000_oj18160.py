dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]
area = 0
def dfs(x, y):
    global area
    # 碰壁时返回
    if board[x][y] == ".":
        return
    # 可达区域标记,防止重复
    board[x][y] = "."
    area += 1
    # 继续尝试搜索
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)


t =int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # 加保护圈
    board = [["." for _ in range(m + 2)]]
    for _ in range(n):
        board.append(["."] + list(input()) + ["."])
    board.append(["." for k in range(m + 2)])
    # 初始化最大面积
    max_area = 0
    # 用for循环遍历,dfs搜索
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] == "W":
                area = 0
                dfs(i, j)
                max_area = max(max_area, area)
    print(max_area)
