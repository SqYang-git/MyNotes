class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                dp[i+1] = dp[i] + 1
        for i in range(n-1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                dp[i - 1] = max(dp[i - 1], dp[i] + 1)
        return sum(dp)
    ans = candy
    print(ans)
    
