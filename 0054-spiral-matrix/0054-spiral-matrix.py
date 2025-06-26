class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d = 0
        tb = 0
        bb = len(matrix)-1
        rb = len(matrix[0])-1
        lb = 0
        a = []
        while len(a)<len(matrix)*len(matrix[0]):
            if d == 0 and len(a)<len(matrix)*len(matrix[0]):
                j = lb
                while j <= rb:
                    a.append(matrix[tb][j])
                    j += 1
                d = 1
                tb += 1
            if d == 1 and len(a)<len(matrix)*len(matrix[0]):
                i = tb
                while i <= bb:
                    a.append(matrix[i][rb])
                    i += 1
                d = 2
                rb -= 1
            if d == 2 and len(a)<len(matrix)*len(matrix[0]):
                j = rb
                while j >= lb:
                    a.append(matrix[bb][j])
                    j-=1
                bb -= 1
                d = 3
            if d==3 and len(a)<len(matrix)*len(matrix[0]):
                i = bb
                while i >= tb:
                    a.append(matrix[i][lb])
                    i-=1
                lb += 1
                d = 0
        return a