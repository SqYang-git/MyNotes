t, M = map(int,input().split())
times = [0] + list(map(int, input().split())) + [M]

tot = 0
for i in range(1, len(times), 2):
    tot += times[i] - times[i-1]

ans = tot  # 初始为总开灯时间

buffer1 = 0
for i in range(2, len(times), 2):
    buffer1 += (times[i - 1] - times[i - 2])  # 维护前i次开灯时间
    if times[i] - times[i-1] >= 2:  # 若可以插入操作,关键判断
        buffer2 = tot - buffer1
        ans = max(ans, buffer1 + (M-times[i-1]) - buffer2 - 1)

print(ans)
