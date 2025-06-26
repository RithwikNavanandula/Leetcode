class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def check(p):
            if p == 0:
                return True
            if p%3 == 0:
                while p%3 == 0:
                    p = p/3
            if p%3 == 2:
                return False
            else:
                return check(p-1)
        return check(n) 
                