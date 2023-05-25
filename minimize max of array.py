class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        div = ceil(sum(nums)/len(nums))
        summ = nums[0]
        ans = [nums[0]]
        for i in range(1,len(nums)):
            summ += nums[i]
            ans.append(math.ceil(summ/(i+1))) 

    
        return max(ans)
        
