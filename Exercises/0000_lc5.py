class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        ans = s[0]
        for i in range(1, n):
            for start in range(n-i):
                sub = s[start:start+i+1]
                if sub == sub[::-1]:
                    ans = sub
                    break
        return ans
