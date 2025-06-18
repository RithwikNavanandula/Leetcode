# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        def summ(l, low, high, k):
            if low <= l.val <= high:
                k += l.val
            if l.left:
                k = summ(l.left, low, high, k) 
            if l.right:
                k = summ(l.right, low, high, k)
            return k
        k = 0
        if root:
            k = summ(root, low, high, k)
        return k