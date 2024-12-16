N = int(input())
heights = list(map(int, input().split()))


def find_dp(heights, N):
    ans = [0] * N
    for i in range(1, N):
        for j in range(i):
            if heights[j] < heights[i]:
                ans[i] = max(ans[i], ans[j] + 1)
    return ans


dp1 = find_dp(heights, N)
heights.reverse()
dp2 = find_dp(heights, N)
dp2.reverse()
for i in range(N):
    dp1[i] += dp2[i]
print(max(dp1)+1)
