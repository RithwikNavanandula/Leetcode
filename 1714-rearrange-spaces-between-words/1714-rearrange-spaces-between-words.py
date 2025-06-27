class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        j = 0
        for i in text:
            if i == " ":
                j += 1
        p = text.split(" ")
        k = 0
        s = []
        for i in p:
            if i.isalpha():
                s.append(i)
        k = len(s)
        if k == 1:
            n = ""
            for i in range(j):
                n+=" "
            return text.strip()+n
        b = j//(k-1)
        c = ""
        for i in range(b):
            c += " "
        p = ""
        d = j%(k-1)
        for i in range(d):
            p+= " "
        l = s[0]
        for i in s[1:]:
            l += c + i
        return l+p
        
