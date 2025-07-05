class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        p = {}
        for i in arr:
            if i in p:
                p[i]+=1
            else:
                p[i] = 1
        k = -1
        for i,j in p.items():
            if i == j:
                k = max(k, i)
        return k