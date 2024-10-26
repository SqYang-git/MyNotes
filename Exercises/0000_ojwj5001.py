def num_ways(gap):
    if gap == 1:
        return 1
    elif gap == 2:
        return 2
    else:
        return num_ways(gap-1) + num_ways(gap-2)


n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    gap = b - a
    print(num_ways(gap))
