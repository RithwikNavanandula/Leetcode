class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        j = 0
        i = 0
        d = 0
        if numRows == 1:
            return s
        k = ['']*(numRows)
        k[i]+=s[j]
        j+=1
        while j < len(s):
            if d == 0:
                if i == numRows-1:
                    i = i-1
                    d = 1
                else:
                    i+=1
            else:
                if i == 0:
                    i = 1
                    d = 0
                else:
                    i -=1
                
            k[i]+=s[j]
            j+=1
        m = ''.join(v for v in k)
        return m