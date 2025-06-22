class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        x = 0
        p = []
        while x < len(s):
            if x+k < len(s):
                p.append(s[x:x+k])
            else:
                p.append(s[x:])
            x += k
        while len(p[-1]) != k:
            p[-1] += fill
        return p