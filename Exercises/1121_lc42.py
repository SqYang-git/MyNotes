class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += right_max - height[right]

        return ans
    answer = trap
    print(answer)
