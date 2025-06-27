class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        des = []
        sor = []
        for i in paths:
            if i[1] not in des:
                des.append(i[1])
            if i[0] in des:
                des.remove(i[0])
            else:
                sor.append(i[0])
            
        for i in sor:
            if i in des:
                des.remove(i)
        return des[0]
            