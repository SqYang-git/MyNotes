n, m = map(int, input().split())
plans = [tuple(map(int, input().split())) for _ in range(n)]
circum = []
for x, width in plans:
    for start in range(max(0, x - width + 1), min(m, x + 1)):
        end = start + width
        if end <= m:
            circum.append((start, end))
circum.sort(key=lambda x: (x[1], x[0]))
cnt = 0
last_end = 0
for start, end in circum:
    if start >= last_end:
        last_end = end
        cnt += 1
print(cnt)
