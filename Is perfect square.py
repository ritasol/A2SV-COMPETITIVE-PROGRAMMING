class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 or num == 0:
            return True
        l,r=2,num

        while l < r:
            mid = (l+r)//2
            if mid **2 == num:
                return True
            elif mid **2 > num:
                r =mid
            else:
                l = mid + 1
