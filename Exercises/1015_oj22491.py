h = int(input())
m = int(input())
eh = 2 * h - m * 0.5
list_rate_maxh = []
for _ in range(m):
    s, c = map(float, input().split())
    rate = s * c
    maxh = 5 / s
    list_rate_maxh.append((rate, maxh))
list_rate_maxh.sort(reverse=True)
sum = 0
for rate, maxh in list_rate_maxh:
    if eh >= maxh:
        sum += rate * maxh
        eh -= maxh
    else:
        sum += rate * eh
        break
print(f"{sum:.1f}")
