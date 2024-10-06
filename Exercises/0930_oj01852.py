num = int(input())
for i in range(num):
    l, n = map(int, input().split())
    x = map(int, input().split())
    min_t = max_t = 0
    for j in x:
        min_t = max(min_t, min(j, l - j))
        max_t = max(max_t, max(j, l - j))

    print(min_t, max_t)
