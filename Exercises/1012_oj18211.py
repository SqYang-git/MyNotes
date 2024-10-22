p = int(input())
cost = list(map(int, input().split()))
cost.sort()

gap = 0
left = 0
right = len(cost) - 1

while left <= right:
    if cost[left] <= p:  # 继续制作
        p -= cost[left]
        gap += 1
        left += 1
    else:
        if left == right:  # 钱不够,但是没得做了
            break
        p += cost[right]  # 卖图纸
        right -= 1
        gap -= 1
        if gap < 0:  # 任一时刻差距不能为负(题干要求)
            gap = 0
            break

print(gap)
