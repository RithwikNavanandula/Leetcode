# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        k = head
        p = 0
        while head:
            p+=1
            head = head.next
        p = p//2
        for i in range(p):
            k = k.next
        return k