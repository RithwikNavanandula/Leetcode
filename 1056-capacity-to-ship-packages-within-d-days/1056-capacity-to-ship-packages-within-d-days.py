class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def check(l):
            x = 0
            c = 1
            for i in weights:
                if x+i>l:
                    x=i
                    c+=1
                else:
                    x+=i
            if c > days:
                return False
            return True
                           
        l = max(weights)
        r = sum(weights)
        while l<r:
            mid = (l+r)/2
            if check(mid):
                r = mid
            else:
                l = mid +1
        return l