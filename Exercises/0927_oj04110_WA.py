n, w = map(int, input().split())
gifts = []
for _ in range(n):
    a, b = map(int, input().split())
    gifts.append([a, b])
value = [[0] * (w + 1) for _ in range(len(gifts) + 1)]
for i in range(1, len(gifts) + 1):
    for j in range(1, w + 1):
        if j < gifts[i - 1][1]:
            value[i][j] = value[i - 1][j]
        else:
            value[i][j] = max(value[i - 1][j], value[i - 1][j - gifts[i - 1][1]] + gifts[i - 1][0])
ans = max(value[-1])
print("%.1f" % ans)
