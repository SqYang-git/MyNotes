n, m = map(int, input().split())
map1 = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if map1[i][j] == 1:
            count += 4
            if i > 0 and map1[i-1][j] == 1:
                count -= 2
            if j > 0 and map1[i][j-1] == 1:
                count -= 2
print(count)
