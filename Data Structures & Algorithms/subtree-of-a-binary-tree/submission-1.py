# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def inorder(self, root):
        """
        Inorder traversal: left subtree, root, right subtree.
        For BST, gives sorted order.
        """
        if not root:
            return ['a']

        result = []
        result.append(root.val)               # Root

        result.extend(self.inorder(root.left))    # Left
        result.extend(self.inorder(root.right))   # Right

        return result

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = self.inorder(p)
        q_list = self.inorder(q)

        # print(p_list)
        # print(q_list)

        return p_list == q_list    

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check all nodes in root
        # if a node in root is same val as subroot's head, check if same tree
        if not root:
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)







        