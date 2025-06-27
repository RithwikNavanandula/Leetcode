class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        def zeros(l):
            k = 0
            for i in l:
                if i == '0':
                    k += 1
            return k
        
        def ones(p):
            k = 0
            for i in p:
                if i == '1':
                    k += 1
            return k
        maxi = 0
        for i in range(1, len(s)):
            maxi = max(maxi, zeros(s[:i])+ones(s[i:]))
        return maxi
        