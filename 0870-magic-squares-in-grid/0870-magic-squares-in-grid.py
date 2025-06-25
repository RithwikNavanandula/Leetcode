class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def magicsquare(i, j):
            p = []
            q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3):
                p.append(grid[i-1+k][j-1])
                p.append(grid[i-1+k][j])
                p.append(grid[i-1+k][j+1])
            p.sort()
            if q == p:
                return True
            return False

        def sumcheck(i,j):
            rsum = 0
            for k in range(3):
                rsum += grid[i-1][j-1+k]
            s = 0
            for k in range(3):
                s += grid[i][j-1+k]
            if s != rsum:
                return False
            s = 0
            for k in range(3):
                s += grid[i+1][j-1+k]
            if s != rsum:
                return False
            s = 0
            for k in range(3):
                s += grid[i-1+k][j-1]
            if s != rsum:
                return False
            s = 0
            for k in range(3):
                s += grid[i-1+k][j]
            if s != rsum:
                return False
            s = 0
            for k in range(3):
                s += grid[i-1+k][j+1]
            if s != rsum:
                return False
            l = -1
            r = 1
            d1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
            d2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
            if d1 == d2 and d2 == rsum:
                return True
            return False
        ans = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if magicsquare(i,j):
                    if sumcheck(i,j):
                        ans+=1
        return ans