class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [set(),set()]
        for i in nums1:
            if i not in nums2:
                ans[0].add(i)
        for i in nums2:
            if i not in nums1:
                ans[1].add(i)
        return ans
