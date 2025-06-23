class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        p = {
            "b" : 0,
            "a" : 0,
            "l" : 0,
            "o" : 0,
            "n" : 0
        }
        for i in text:
            if i in p:
                p[i] += 1
        p["l"] /=2
        p["o"] /= 2
        return min(p.values())