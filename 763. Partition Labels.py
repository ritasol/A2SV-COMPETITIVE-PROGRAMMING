class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict = {}
        ans = []
        right= -1
        left = 0
        for i , m in enumerate (s):
            dict[m] = i
        for i , m in enumerate (s):
            left = max(left,dict[m])
            if left == i:
                ans.append(i-right)
                right = i
        return ans