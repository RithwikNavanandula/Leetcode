class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def function(i, j):
            for l in range(rows):
                matrix[l][j] = 0
            for n in range(columns):
                matrix[i][n] = 0
        rows = len(matrix)
        columns = len(matrix[0])
        p = []
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    p.append([i,j])
        for i in range(len(p)):
                function(p[i][0], p[i][1])