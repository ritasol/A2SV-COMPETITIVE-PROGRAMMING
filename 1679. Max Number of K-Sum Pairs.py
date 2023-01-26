class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while left < right :
            sum = nums[left]+nums[right]
            if sum == k:
                count+= 1
                left += 1
                right -= 1
            elif sum < k :
                left += 1
            else :
                right -= 1
        return count
                