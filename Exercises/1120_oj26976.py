n = int(input())
list_num= list(map(int, input().split()))
dp1 = [1] * n
for i in range(n):
    max_len = 1
    for j in range(i):
        if list_num[j] < list_num[i] and dp1[j] + 1 > max_len and dp1[j] % 2 == 1:
            max_len = dp1[j] + 1
        if list_num[j] > list_num[i] and dp1[j] + 1 > max_len and dp1[j] % 2 == 0:
            max_len = dp1[j] + 1
    dp1[i] = max_len
dp2 = [1] * n
for i in range(n):
    max_len = 1
    for j in range(i):
        if list_num[j] < list_num[i] and dp2[j] + 1 > max_len and dp2[j] % 2 == 0:
            max_len = dp2[j] + 1
        if list_num[j] > list_num[i] and dp2[j] + 1 > max_len and dp2[j] % 2 == 1:
            max_len = dp2[j] + 1
    dp2[i] = max_len
ans = max(max(dp1), max(dp2))
print(ans)
