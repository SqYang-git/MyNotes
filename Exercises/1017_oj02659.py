a, b, k = map(int, input().split())
field = [[0] * b for _ in range(a)]
for _ in range(k):
    r, s, p, t = map(int, input().split())
    r -= 1
    s -= 1
    half = p // 2
    for i in range(max(0, r - half), min(a, r + half+1)):
        for j in range(max(0, s - half), min(b, s + half+1)):
            if t == 1:
                if field[i][j] != -1:
                    field[i][j] += 1
            else:
                field[i][j] = -1

count = 0
max_value = 0
for i in range(a):
    for j in range(b):
        if field[i][j] > max_value:
            max_value = field[i][j]
            count = 1
        elif field[i][j] == max_value and max_value != 0:
            count += 1
print(count)
