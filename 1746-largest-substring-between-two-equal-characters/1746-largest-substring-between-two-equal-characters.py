class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = {}
        k = -1
        for i in range(len(s)):
            if s[i] in p:
                k = max(i-p[s[i]]-1, k)
            else:
                p[s[i]] = i
        return k