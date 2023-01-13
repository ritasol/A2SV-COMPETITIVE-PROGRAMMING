class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(nums):
            if target in nums[i]:
                return True
            elif target not in nums[i] and nums[i][-1] < target:
                i += 1
            elif target not in nums[i] and nums[i][-1] > target:
                break
        return False

