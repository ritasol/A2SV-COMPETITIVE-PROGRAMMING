class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort(reverse=True)
        ans = [] 
        for i in range(len(nums)):
            if target == nums[i]:
                ans.append(i)
            elif nums[i] > target:
                break
        return ans
            
        
        