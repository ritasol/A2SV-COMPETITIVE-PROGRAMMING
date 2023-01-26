class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        fast=1
        while(fast < len(nums)):
            if(nums[fast] == nums[fast-1] ):
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1
        print(nums)
        return slow+1
