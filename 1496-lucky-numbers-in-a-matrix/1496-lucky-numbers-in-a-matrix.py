class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        mr = []
        ans = []
        for i in matrix:
            mr.append(min(i))
        p = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                p[j] = max(p[j], matrix[i][j])
        for i in mr:
            if i in p:
                ans.append(i)
        return ans