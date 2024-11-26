dp = [1, 1, 2] + [0] * 23
for i in range(3, 26):
    dp[i] = sum(dp[j] for j in range(i))
n = int(input())
print(dp[n])
