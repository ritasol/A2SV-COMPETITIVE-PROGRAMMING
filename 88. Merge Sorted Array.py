class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lst = nums1[:m]
        i = 0
        j = 0
        k = 0

        while i < len(lst) and j < n:
            if lst[i] < nums2[j]:
                nums1[k] = lst[i]
                i += 1
            
            else:
                nums1[k] = nums2[j]
                j += 1
            
            k += 1
        
        while i < len(lst):
            nums1[k] = lst[i]
            
            i += 1
            k += 1
        
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
