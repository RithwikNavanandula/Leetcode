class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        p = []
        for i in emails:
            k = i.split('@')
            k[0] = k[0].replace(".", "")
            if '+' in k[0]:
                k[0] = k[0].split('+')[0]
            if k[0] + '@'+ k[1] not in p:
                p.append(k[0]+'@'+k[1])
        return len(p)