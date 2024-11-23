class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        nums.index(target)
        left = nums.index(target)
        nums.reverse()
        right = len(nums) - nums.index(target) - 1
        return [left, right]