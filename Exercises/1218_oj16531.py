m, n = map(int, input().split())
stu_ind = []
for _ in range(m):
    line = list(map(int, input().split()))
    stu_ind.append(line)
stu_circum = []
stu_mark = []
for _ in range(m*n):
    circum = input()
    stu_circum.append(circum)
    mark = sum(map(int, circum.split()))
    stu_mark.append(mark)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
for i in range(m):
    for j in range(n):
        ind_0 = stu_ind[i][j]
        circum_0 = stu_circum[ind_0]
        same = False
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if stu_circum[stu_ind[nx][ny]] == circum_0:
                    same = True
                    break
        if same:
            count += 1
stu_mark.sort(reverse=True)
min_mark = stu_mark[0]
index = 0
while index < m*n:
    num = stu_mark[index:].count(min_mark)
    if index + num > m*n*0.4:
        print(f"{count} {index}")
        exit()
    index += num
    min_mark = stu_mark[index]
