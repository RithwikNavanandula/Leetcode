class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        s = palindrome
        if s != s[::-1]: 
            return s

        if len(palindrome) == 1:
            return ""

        for i in range(len(s)):
            if s[i] != 'a': 
                s = s[:i] + 'a' + s[i+1:]
                if s == s[::-1]: 
                    return palindrome[:len(palindrome)-1] + 'b'
                return s

        s = s[:-1] + 'b'
        return s
