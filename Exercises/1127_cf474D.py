modulo = 1000000007
t, k = map(int, input().split())
dp = [1] * k + [0] * (100001 - k)
for i in range(k, 100001):
    dp[i] = (dp[i-1] + dp[i-k]) % modulo
buffer = [0] * 100001
for i in range(1, 100001):
    buffer[i] = (buffer[i-1] + dp[i]) % modulo
for i in range(t):
    a, b = map(int, input().split())
    print((buffer[b] - buffer[a-1] + modulo) % modulo)
