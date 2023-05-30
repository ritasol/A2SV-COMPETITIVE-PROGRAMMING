class Solution:
    def helper(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        res = self.helper(n-1) + self.helper(n-2) + self.helper(n-3)
        self.cache[n] = res
        return res
    
    def tribonacci(self, n: int) -> int:
        self.cache = {}
        return self.helper(n)
    
