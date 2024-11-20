dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
min_steps = float('inf')


def dfs(TreasureMap, x, y, steps):
    global min_steps
    if steps >= min_steps:
        return
    if TreasureMap[x][y] == 1:
        min_steps = steps
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 这里忘了加一个判断是否将要到达终点的条件结果错了半天,还怪难检查的😅
        if TreasureMap[nx][ny] == 0 or TreasureMap[nx][ny] == 1:
            buffer = TreasureMap[x][y]
            TreasureMap[x][y] = 2
            dfs(TreasureMap, nx, ny, steps + 1)
            TreasureMap[x][y] = buffer


m, n = map(int, input().split())
TreasureMap = [[2 for _ in range(n + 2)]]
for i in range(m):
    TreasureMap.append([2] + list(map(int, input().split())) + [2])
TreasureMap.append([2 for _ in range(n + 2)])
dfs(TreasureMap, 1, 1, 0)
print(min_steps if min_steps != float('inf') else "NO")
