class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(original):
            return []
        r = 0
        c = 1
        a = [[]]
        for i in original:
            if c != n+1:
                a[r].append(i)
                c += 1
            else:
                c = 2
                a.append([])
                r +=1
                a[r].append(i)
        return a


