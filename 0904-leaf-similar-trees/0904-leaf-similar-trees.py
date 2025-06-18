# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(l, p):
            if not l.left and not l.right:
                p.append(l.val)
            else:
                if l.left:
                    p = dfs(l.left, p)
                if l.right:
                    p = dfs(l.right, p)
            return p
        k1 = []
        k2 = []
        if root1:
            k1 = dfs(root1, k1)
        if root2:
            k2 = dfs(root2, k2)
        return k1==k2

                    
