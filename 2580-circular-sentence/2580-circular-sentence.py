class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s = sentence.split(" ")
        for i in range(len(s)):
            if i == len(s)-1:
                if s[i][-1] != s[0][0]:
                    return False
            elif s[i][-1] != s[i+1][0]:
                return False
        return True