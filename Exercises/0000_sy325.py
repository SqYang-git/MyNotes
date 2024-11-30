from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(start, end, portal1, portal2, maze):
    queue = deque([(0, start)])
    in_queue = {start}
    while queue:
        step, (x, y) = queue.popleft()
        if (x, y) == end:
            return step
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((nx, ny) == portal1 and portal2 not in in_queue) or ((nx, ny) == portal2 and portal1 not in in_queue):
                queue.append((step + 1, portal2))
                queue.append((step + 1, portal1))
                in_queue.add(portal2)
                in_queue.add(portal1)
            if maze[nx][ny] == 0 and (nx, ny) not in in_queue:
                queue.append((step + 1, (nx, ny)))
                in_queue.add((nx, ny))
    return float("inf")


n, m = map(int, input().split())
portals = []
maze = [[1] * (m + 2)]
for i in range(1, n+1):
    line = [1]+list(map(int, input().split()))+[1]
    try:
        portals.append((i, line.index(2)))
    except ValueError:
        pass
    maze.append(line)
maze.append([1] * (m+2))
portal1 = portals[0]; portal2 = portals[1]
ans = bfs((1, 1), (n, m), portal1, portal2, maze)
print(ans if ans != float("inf") else "-1")
