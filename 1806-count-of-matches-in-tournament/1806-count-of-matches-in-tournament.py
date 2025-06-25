class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        while n != 1:
            m+=(n//2)
            if n%2 != 0 : n +=1
            n = n//2
        return m