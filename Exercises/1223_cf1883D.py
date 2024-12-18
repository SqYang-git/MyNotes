import heapq
from collections import defaultdict
q = int(input())
intervals = []
left_set = defaultdict(int)
right_set = defaultdict(int)
min_r = []
max_l = []
for _ in range(q):
    operate = input().split()
    l, r = int(operate[1]), int(operate[2])
    if operate[0] == "+":
        left_set[l] += 1
        right_set[r] += 1
        heapq.heappush(max_l, -l)
        heapq.heappush(min_r, r)
    else:
        left_set[l] -= 1
        right_set[r] -= 1
    # 清除堆中无效边界
    while max_l and left_set[-max_l[0]] <= 0:
        heapq.heappop(max_l)
    while min_r and right_set[min_r[0]] <= 0:
        heapq.heappop(min_r)
    # 贪心策略:若最小右边界小于最大左边界,存在不重叠的一组区间
    if max_l and min_r and min_r[0] < -max_l[0]:
        print("YES")
    else:
        print("NO")
