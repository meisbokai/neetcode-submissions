# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST - ordered (left, root, right)

        while True:
            if root.val < min(p.val, q.val):
                # look to the right
                root = root.right
            elif root.val > max(p.val, q.val):
                # look to the left
                root = root.left
            else:
                return root


