# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(i, j):
            p = 1
            if max(i,j)%min(i,j) == 0: return min(i,j)
            for k in range(1, min(i, j)):
                if i%k == 0 and j%k == 0:
                    p = k
            return p
        p = n = head
        n = n.next
        while n:
            k = gcd(p.val, n.val)
            node = ListNode()
            node.val = k
            p.next = node
            node.next = n
            p = n
            n = n.next
        return head