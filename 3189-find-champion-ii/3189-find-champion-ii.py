class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = {}
        for i in range(n):
            p[i] = 0
        for i in edges:
            if p[i[1]] == 0:
                p[i[1]] = 1
        l = []
        for key, value in p.items():
            if value == 0:
                l.append(key)
        if len(l) == 1:
            return l[0]
        return -1
