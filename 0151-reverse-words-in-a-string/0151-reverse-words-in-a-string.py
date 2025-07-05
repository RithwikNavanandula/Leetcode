class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = s.strip(" ").split()
        while "" in p:
            p.remove("")
        p = p[::-1]
        k = ''
        for i in p:
            k+=i
            k+=" "
        return k[:-1]