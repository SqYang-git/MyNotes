from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(map1, start, end):
    queue = deque([(0, start)])
    in_queue = {start}
    while queue:
        step, (x, y) = queue.popleft()
        if (x, y) == end:
            return step
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) not in in_queue and map1[nx][ny] != "#":
                step_add = abs(int(map1[nx][ny]) - int(map1[x][y]))
                queue.append((step + step_add, (nx, ny)))
                in_queue.add((nx, ny))
    return "NO"


m, n, p = map(int, input().split())
map1 = [["#"]*(n + 2)]
for _ in range(m):
    map1.append(["#"]+list(input().split())+["#"])
map1.append(["#"]*(n + 2))
for _ in range(p):
    xs, ys, xe, ye = map(int, input().split())
    start = (xs, ys)
    end = (xe, ye)
    if map1[xs][ys] == "#" or map1[xe][ye] == "#":
        print("NO")
        continue
    print(bfs(map1, start, end))
