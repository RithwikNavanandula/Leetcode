class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = []
        l = 0
        r = len(mat)-1
        for i in mat:
            res.append(i[l])
            res.append(i[r])
            l += 1
            r -= 1
        if len(mat)%2 ==0: return sum(res)
        return sum(res) - mat[l//2][l//2]