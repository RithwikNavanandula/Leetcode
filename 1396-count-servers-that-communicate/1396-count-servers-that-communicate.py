class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def com(i, j):
            for k in range(len(grid)):
                if k != i and grid[k][j] == 1:
                    return 1
            for k in range(len(grid[0])):
                if k!= j and grid[i][k] == 1:
                    return 1
            return 0
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    n += com(i, j)
        return n


        