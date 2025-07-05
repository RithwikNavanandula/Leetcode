class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        p = []
        k = path.split("/")
        while "" in k:
            k.remove("")
        for i in k:
            if i == "..":
                p = p[:-2]
            elif i == ".":
                continue
            else:
                p.append(i)
                p.append("/")
        b = '/'
        for i in p:
            b+=i
        if b[-1] == "/" and b != "/": return b[:-1]
        return b