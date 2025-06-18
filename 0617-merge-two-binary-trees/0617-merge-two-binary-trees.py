# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root2:
            return root1
        if not root1 and root2:
            root1 = root2
        elif root1 and root2:
            root1.val += root2.val
        if root1.left and root2.left:
            self.mergeTrees(root1.left, root2.left)
        elif not root1.left and root2.left:
            root1.left = root2.left
        if root1.right and root2.right:
            self.mergeTrees(root1.right, root2.right)
        elif not root1.right and root2.right:
            root1.right = root2.right
        return root1