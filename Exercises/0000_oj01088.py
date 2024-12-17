r, c = map(int, input().split())
node = [[100001 for _ in range(c + 2)]]
for _ in range(r):
    row = [int(x) for x in input().split()]
    node.append([100001] + row + [100001])
node.append([100001 for _ in range(c + 2)])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
step = [[0] * (c + 2) for _ in range(r + 2)]


def dfs(i, j):
    if step[i][j] > 0:
        return step[i][j]
    step[i][j] = 1
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 1 <= nx <= r and 1 <= ny <= c and node[nx][ny] > node[i][j]:
            step[i][j] = max(step[i][j], dfs(nx, ny) + 1)
    return step[i][j]


ans = 0
for i in range(1, r + 1):
    for j in range(1, c + 1):
        ans = max(ans, dfs(i, j))

print(ans)
