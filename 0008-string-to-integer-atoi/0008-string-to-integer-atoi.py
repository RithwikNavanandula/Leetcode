class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        
        k = False
        if s[0] == "-":
            k = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        if not s or not s[0].isnumeric():
            return 0
        
        b = s
        for i in range(len(s)):
            if not s[i].isnumeric():
                b = s[:i]
                break

        if not b:
            return 0
        
        result = int(b)
        if k:
            result = -result

        result = max(min(result, 2**31 - 1), -2**31)
        return result
