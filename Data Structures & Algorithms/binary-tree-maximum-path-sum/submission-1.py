# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans=float("-inf")

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            left=max(0,left)
            right=max(0,right)

            summ=node.val+left+right

            ans=max(ans,summ)

            return node.val + max(left,right)
        
        dfs(root)

        return ans