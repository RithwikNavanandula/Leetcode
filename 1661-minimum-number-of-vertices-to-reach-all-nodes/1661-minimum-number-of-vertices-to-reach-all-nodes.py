class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = [0]*n
        b = []
        for i in edges:
            if p[i[1]] == 0:
                p[i[1]] = 1
        for i in range(n):
            if p[i] == 0:
                b.append(i)
        return b