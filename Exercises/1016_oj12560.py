n, m = map(int, input().split())
list_0 = []
for _ in range(n):
    list_buffer = list(map(int, input().split()))
    list_0.append(list_buffer)
list_1 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        sum_around = 0
        for a in range(max(i-1, 0), min(i+2, n)):
            for b in range(max(j-1, 0), min(j+2, m)):
                sum_around += list_0[a][b]
        if list_0[i][j] == 1:
            if sum_around < 3:
                list_1[i][j] = 0
            elif sum_around == 3 or sum_around == 4:
                list_1[i][j] = 1
            else:
                list_1[i][j] = 0
        else:
            if sum_around == 3:
                list_1[i][j] = 1
for line in list_1:
    print(*line)
