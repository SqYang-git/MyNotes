from collections import deque

def bfs(n): # 定义bfs函数,变量为终点
    queue = deque([(0, 1)])  # 原点入队,步长为0,数值为1
    in_queue = {1}  # 原点标记为已入队
    while queue:
        # 取出front元素及其步数
        step, front = queue.popleft()
        # 如果front元素达到预期数字,输出步数
        if front == n:
            return step
        # 若结点“乘2”未入队,加入队列,并标记为已入队
        buffer1 = front * 2; buffer2 = front + 1
        if buffer1 <= n and buffer1 not in in_queue:
            in_queue.add(buffer1)
            queue.append((step + 1, buffer1))
        # 若结点“加1”未入队,加入队列,并标记为已入队
        if buffer2 <= n and buffer2 not in in_queue:
            in_queue.add(buffer2)
            queue.append((step + 1, buffer2))


print(bfs(int(input())))
