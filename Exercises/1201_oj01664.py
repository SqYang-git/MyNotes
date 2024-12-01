ans = 0
visited = []


def dfs(start, M, N, step):
    global ans, visited
    if step == M:
        way = sorted(start)
        if way not in visited:
            visited.append(way)
            ans += 1
        return
    for i in range(N):
        buffer = start[:]
        buffer[i] += 1
        buffer.sort()
        if buffer not in visited:
            dfs(buffer, M, N, step + 1)
            visited.append(buffer)


t = int(input())
for _ in range(t):
    M, N = map(int, input().split())
    dfs([0] * N, M, N, 0)
    print(ans)
    ans = 0
    visited = []
