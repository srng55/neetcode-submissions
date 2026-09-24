# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return None

        # ROOT
        root = TreeNode(preorder[0])

        # FIND ROOT IN INORDER
        root_index = inorder.index(root.val)

        # LEFT
        left_preorder = preorder[1:root_index + 1]
        left_inorder = inorder[:root_index]

        root.left = self.buildTree(
            left_preorder,
            left_inorder
        )

        # RIGHT
        right_preorder = preorder[root_index + 1:]
        right_inorder = inorder[root_index + 1:]

        root.right = self.buildTree(
            right_preorder,
            right_inorder
        )

        return root