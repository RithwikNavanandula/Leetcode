class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        k = [0, 0]
        p = []
        p.append(deepcopy(k))
        for i in path:
            if i == "N":
                k[1]+= 1
                if k in p:
                    return True
                p.append(deepcopy(k))
            elif i == "E":
                k[0]+= 1
                if k in p:
                    return True
                p.append(deepcopy(k))
            elif i == "S":
                k[1]-= 1
                if k in p:
                    return True
                p.append(deepcopy(k))
            elif i == "W":
                k[0]-= 1
                if k in p:
                    return True
                p.append(deepcopy(k))
        return False