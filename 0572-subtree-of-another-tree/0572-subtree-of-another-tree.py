# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            if p.val!=q.val:
                return False
            if  not dfs(p.left, q.left) or not dfs(p.right, q.right):
                return False
            return True
        
        
        
        def check(l, k):
            d = False
            if not l:
                return 
            if l.val == k.val:
                d = dfs(l, k)
            if d == True:
                return d
            if l.left and l.right:
                return check(l.left, k) or check(l.right, k)
            else:
                if l.left:
                    return check(l.left, k)
                else:
                    return check(l.right, k)

        if root:
            c =  check(root, subRoot)
        if c:
            return True
        if not subRoot:
            return True
        return False
            