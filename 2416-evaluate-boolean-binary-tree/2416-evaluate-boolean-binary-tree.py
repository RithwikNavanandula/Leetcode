# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(l):
            if not l:
                return 
            if l.val == 0 or l.val == 1:
                return l.val
            else:
                if l.val == 2:
                    return dfs(l.left) | dfs(l.right)
                else:
                    return dfs(l.left) & dfs(l.right)
        if root:
            p = dfs(root)
        if p == 1:
            return True
        return False
         