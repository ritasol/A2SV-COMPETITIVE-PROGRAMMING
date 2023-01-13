class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        for i in strs:
            col = len(i)
        row = len(strs)
        cnt = 0
        for i in range(col):
            a = ""
            for j in range(row):
                a += strs[j][i]
        
            
            if "".join(sorted(a)) != a:
                cnt += 1
        
        return cnt