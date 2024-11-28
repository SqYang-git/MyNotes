from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(start,end,maze):
    queue = deque([(0, start)])
    in_queue = {start}
    while queue:
        step, (x, y) = queue.popleft()
        if (x, y) == end:
            return step
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if maze[nx][ny] != "*" and (nx, ny) not in in_queue:
                queue.append((step + 1, (nx, ny)))
                in_queue.add((nx, ny))
    return -1


n, m = map(int, input().split())
maze = [["*"] * (m + 2)]
for i in range(1, n+1):
    line = input()
    if line.find("S") != -1:
        start = (i, line.find("S") + 1)
    if line.find("T") != -1:
        end = (i, line.find("T") + 1)
    maze.append(["*"] + list(line) + ["*"])
maze.append(["*"] * (m + 2))
print(bfs(start,end,maze))
