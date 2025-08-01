class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def is_prime(num):
            for i in range(2, num/2):
                if num%i==0:
                    return False
            return True
        
        if n<=0:
            return False
        
        while n%2 == 0:
            n = n/2
        while n%3 == 0:
            n = n/3
        while n%5 == 0:
            n = n/5
        if n == 1: return True
        return False
            