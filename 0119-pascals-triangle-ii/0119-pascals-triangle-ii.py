class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        p1 = [1, 1]
        if rowIndex <2:
            if rowIndex == 1:
                return p1
            else:
                return [1]
        n = rowIndex
        while n > 1:
            k = [1]
            i = 0
            while i < len(p1) - 1:
                k.append(p1[i]+p1[i+1])
                i += 1
            p1 = k + [1]
            n -=1
        return p1 