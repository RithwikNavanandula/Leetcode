class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        for i in range(cols):
            x =[]
            for j in range(rows):
                x.append(matrix[j][i])
            ans.append(x)
                
        return ans