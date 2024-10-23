n = int(input())
segments = []
for i in range (n):
    x, h = map(int, input().split())
    segments.append([x-h, x+h])

count = 1
left = (segments[0][0] + segments[0][1]) // 2
for i in range(1, n):
    if segments[i][0] > left:
        count += 1
        left = (segments[i][0] + segments[i][1]) // 2
    elif i == n-1:
        count += 1
    elif segments[i][1] < (segments[i+1][0] + segments[i+1][1]) // 2:
        count += 1
        left = segments[i][1]
    else:
        left = (segments[i][0] + segments[i][1]) // 2

print(count)

