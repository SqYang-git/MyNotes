n, t = map(int, input().split())
prices = list(map(int, input().split()))
sum_prices = sum(prices)
if t > sum_prices:
    print(0)

dp = [[-float('inf')] * (sum_prices + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(sum_prices + 1):
        if j >= prices[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - prices[i - 1]] + prices[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

for k in range(t, sum_prices + 1):
    if dp[n][k] >= t:
        print(k)
        break
