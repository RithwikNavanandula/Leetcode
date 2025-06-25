class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        k = min(str1, str2)
        p = max(str1, str2)
        l = ""
        for i in range(len(k)):
            if len(k)%(i+1) ==0 and len(p)%(i+1)==0:
                if k[:i+1] == p[:i+1]:
                    l = k[:i+1]
        c =l
        finalans = ""
        while True:
            x = deepcopy(str1)
            y = deepcopy(str2)
            x = x.replace(c, "")
            y = y.replace(c, "")
            if x == "" and y =="":
                finalans = c
                c = c+l
            else:
                break

        return finalans
