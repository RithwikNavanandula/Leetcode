class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = []
        q = []
        r = []
        for i in nums:
            if i > 0:
                p.append(i)
            else:
                q.append(i)
        for i in range(len(p)):
            r.append(p[i])
            r.append(q[i])
        return r