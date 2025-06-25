class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        def maxi(i,j):
            return max(grid[i-1][j-1], grid[i][j-1], grid[i+1][j-1], grid[i-1][j], grid[i][j], grid[i+1][j], grid[i-1][j+1], grid[i][j+1], grid[i+1][j+1])
        r = len(grid)
        c = len(grid[0])
        a = []
        for i in range(1, r-1):
            x = []
            for j in range(1, c-1):
                x.append(maxi(i,j))
            a.append(x)
        return a
