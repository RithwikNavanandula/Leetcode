# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """

        a = [0]*n
        p = []
        for _ in range(m):
            p.append(deepcopy(a))
        
        d = 0
        tb = 0
        bb = m-1
        rb = n-1
        lb = 0
        b = c = head
        count = 1
        while b.next:
            b = b.next
            count += 1
        while count < m*n:
            b.next = ListNode(-1)
            b = b.next
            count+=1


        while c:
            if d == 0 and c:
                j = lb
                while j <= rb and c:
                    p[tb][j] = c.val
                    c = c.next
                    j += 1
                d = 1
                tb += 1
            if d == 1 and c:
                i = tb
                while i <= bb and c: 
                    p[i][rb] = c.val
                    c = c.next
                    i += 1
                d = 2
                rb -= 1
            if d == 2 and c:
                j = rb
                while j >= lb and c: 
                    p[bb][j] = c.val
                    c = c.next
                    j-=1
                bb -= 1
                d = 3
            if d==3 and c:
                i = bb
                while i >= tb and c:
                    p[i][lb] = c.val
                    c = c.next
                    i-=1
                lb += 1
                d = 0
        return p
        