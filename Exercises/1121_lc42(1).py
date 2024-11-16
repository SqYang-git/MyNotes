class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left < right:

            if left_max < right_max:
                left += 1
                # 更新左侧最大高度直至左侧最大高度大于等于右侧最大高度,进入下一情况
                left_max = max(left_max, height[left])
                # 若递增,不积攒雨水,若递减,积攒雨水
                ans += left_max - height[left]
            else:
                right -= 1
                # 更新右侧最大高度直至右侧最大高度大于等于左侧最大高度,返回上一情况
                right_max = max(right_max, height[right])
                # 若递增,不积攒雨水,若递减,积攒雨水
                ans += right_max - height[right]

        return ans
    answer = trap
    print(answer)
