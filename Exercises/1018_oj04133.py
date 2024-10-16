d = int(input())
n = int(input())
street = []
for _ in range(1025):
    street.append([0] * 1025)
for _ in range(n):
    x, y, k = map(int, input().split())
    for i in range(max(0, x-d), min(1025, x+d+1)):
        for j in range(max(0, y-d), min(1025, y+d+1)):
            street[i][j] += k

count = 0
max_value = 0
for i in range(1025):
    for j in range(1025):
        if street[i][j] > max_value:
            max_value = street[i][j]
            count = 1
        elif street[i][j] == max_value:
            count += 1
print(count, max_value)
