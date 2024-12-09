n = int(input())
potions = [0] + list(map(int, input().split()))
dp = [-1] * (n + 1)
dp[0] = 0
for j in range(1, n + 1):
    for i in range(j, 0, -1):
        if dp[i - 1] >= 0:
            dp[i] = max(dp[i], dp[i - 1] + potions[j])
for i in range(n, -1, -1):
    if dp[i] >= 0:
        print(i)
        break
