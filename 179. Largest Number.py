class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
        def mycmp(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0
        ans = sorted(nums , key=cmp_to_key(mycmp))
        return str(int("".join(ans)))