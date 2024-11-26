n = int(input())
dp = [0] * 5001
dp[0] = 1
dp[1] = 1
for i in range(2, 5001):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
