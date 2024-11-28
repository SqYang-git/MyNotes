from collections import deque
# 给定行走方案
dx = [0, 0, 1, -1, 0, 0, 2, -2]
dy = [1, -1, 0, 0, 2, -2, 0, 0]


def bfs(start, end, maze):
    # 初始化list-like的双端队列,以及已入队的节点
    queue = deque([(0, start)])
    in_queue = {start}
    while queue:
        # 取出队首元素
        step, (x, y) = queue.popleft()
        # 若达到终点,输出步骤数
        if (x, y) == end:
            return step
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 先尝试访问单步节点是否可通过
            if maze[nx][ny] != 1:
                nnx = x + dx[i + 4]
                nny = y + dy[i + 4]
                # 再尝试跨步节点是否可达到,以及是否已入队
                if maze[nnx][nny] != 1 and (nnx, nny) not in in_queue:
                    # 跨步节点入队
                    queue.append((step + 1, (nnx, nny)))
                    in_queue.add((nnx, nny))
                # 若单步节点未入队,让它入队
                if (nx, ny) not in in_queue:
                    # 单步节点入队
                    queue.append((step + 1, (nx, ny)))
                    in_queue.add((nx, ny))
    # 无法到达终点,输出-1
    return -1


n, m = map(int, input().split())
# 保护圈
maze = [[1] * (m + 2)]
for _ in range(n):
    maze.append([1]+list(map(int, input().split()))+[1])
maze.append([1] * (m+2))
print(bfs((1, 1), (n, m), maze))
