class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        k = 1
        p = []
        m = []
        for i in grid:
            for j in i:
                k += 1
                if j not in p:
                    p.append(j)
                else:
                    m.append(j)
        for i in range(1, k):
            if i not in p:
                m.append(i)
        return m