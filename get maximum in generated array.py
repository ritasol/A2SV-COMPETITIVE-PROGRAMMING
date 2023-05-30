class Solution:
    def helper(self, n: int) -> int:
        if n in self.nums:
            return self.nums[n]
        if n == 0:
            self.nums[0] = 0
            return 0
        if n == 1:
            self.nums[1] = 1
            return 1
        if n % 2 == 0:
            res = self.helper(n//2)
            self.nums[n] = res
        else:
            res = self.helper(n//2) + self.helper((n//2)+1)
            self.nums[n] = res
        return self.nums[n]


    def getMaximumGenerated(self, n: int) -> int:
        self.nums = {}
        for i in range(n+1):
            self.helper(i)
        print(self.nums)
        lst = self.nums.values()
        return max(lst)
