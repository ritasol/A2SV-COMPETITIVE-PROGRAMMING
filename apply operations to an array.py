class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        
        lst = [0] * nums.count(0)
        lst_2 = []
        
        for i in nums:
            if i != 0:
                lst_2.append(i)

        return lst_2 + lst