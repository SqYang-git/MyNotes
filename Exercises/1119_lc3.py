class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0; r = 0
        n = len(s)
        max_len = 0
        seen = set()
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            else:
                seen.remove(s[l])
                l += 1
        return max_len
    ans = lengthOfLongestSubstring
    print(ans)
