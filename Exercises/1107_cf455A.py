n = int(input())
buffer = [0] * 100001
a = list(map(int, input().split()))
for i in range(n):
    buffer[a[i]] += 1

dp = [0] * 100001
for i in range(1, 100001):
    dp[i] = max(dp[i-1], dp[i-2] + buffer[i] * i)

print(max(dp))
