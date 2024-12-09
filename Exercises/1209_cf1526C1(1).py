import heapq


def max_potions(n, potions):
    heap = []
    health = 0
    num = 0
    for effect in potions:
        if health + effect >= 0:  # 喝下不会寄掉
            heapq.heappush(heap, effect)
            health += effect
            num += 1
        # 要是喝下会寄掉,讨论:
        # 当堆非空且替换最差药水可以得到更好的健康值,那就换掉
        elif heap and effect > heap[0]:
            health -= heapq.heappop(heap)  # 弹出最差的药水
            heapq.heappush(heap, effect)  # 加入新的药水
            health += effect
    return num


n = int(input())
potions = list(map(int, input().split()))
print(max_potions(n, potions))
