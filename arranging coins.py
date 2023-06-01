class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins = n
        cnt = 0
        if n == 1:
            return 1
        for i in range(1,n):
            coins -= i
        
            if coins < 0:
                return cnt
            else:
                cnt += 1
        return cnt
