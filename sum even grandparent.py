class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,dad,gp):
            if not root:
                return 0
            x=0
            if(gp%2==0):
                x=root.val
            x+=dfs(root.left,root.val,dad)
            x+=dfs(root.right,root.val,dad)
            return x

        return dfs(root,1,1)
