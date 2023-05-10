# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, maxi = 0):
        self.maxi = maxi

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            
            lh = helper(root.left)
            rh = helper(root.right)
        
            self.maxi = max(self.maxi, lh + rh)

            return 1 + max(lh, rh)
        
        helper(root)
        return self.maxi
