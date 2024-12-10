import heapq
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dijkstra(xs, ys, xe, ye):
    if region[xs][ys] == "#" or region[xe][ye] == "#":
        return "NO"
    if (xs, ys) == (xe, ye):
        return 0
    pq = []  # 初始化堆
    heapq.heappush(pq, (0, xs, ys))  # (体力消耗, x坐标, y坐标)
    visited = set()  # 不重复的已访问元素集
    efforts = [[float('inf')] * n for _ in range(m)]  # 到达图中位置需要的体力,初始化为inf,即不可达到
    efforts[xs][ys] = 0  # 初始化体力记录表
    while pq:
        current_effort, x, y = heapq.heappop(pq)  # 取出堆顶元素
        if (x, y) in visited:
            continue
        # 未访问过,进一步操作:
        visited.add((x, y))
        # 达到终点则返回
        if (x, y) == (xe, ye):
            return current_effort
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if region[nx][ny] == "#":
                    continue
                effort = current_effort + abs(int(region[x][y]) - int(region[nx][ny]))
                if effort < efforts[nx][ny]:
                    efforts[nx][ny] = effort
                    # 放入堆中
                    heapq.heappush(pq, (effort, nx, ny))
    # 无法达到
    return "NO"


m, n, p = map(int, input().split())
region = []
for _ in range(m):
    region.append(input().split())
task = []
for _ in range(p):
    task.append(tuple(map(int, input().strip().split())))
for xs, ys, xe, ye in task:
    print(dijkstra(xs, ys, xe, ye))
