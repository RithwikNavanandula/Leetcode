class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        p = {}
        for i in words:
            for j in i:
                if j not in p:
                    p[j] = 1
                else:
                    p[j] += 1
        for i in p.values():
            if i%len(words)!= 0:
                return False
        return True