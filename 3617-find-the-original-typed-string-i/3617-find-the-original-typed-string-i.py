class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        p = word[0]
        for i in word:
            if i != p[-1]:
                p+=i
        return len(word)-len(p)+1