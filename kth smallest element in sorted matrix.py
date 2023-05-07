class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst=[]
        for i in matrix:
            lst.extend(i)
        lst.sort()
        return lst[k-1]
        
