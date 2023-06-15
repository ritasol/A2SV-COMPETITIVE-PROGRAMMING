# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        cnt = []
    
        
        while queue:
            summ = 0
            for _ in range(len(queue)):
                curr = queue.popleft()
                summ += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            cnt.append(summ)     
        return cnt.index(max(cnt))+1

                
                
                
                    
                
