class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        d = 0
        b = 0
        while numBottles != 0:
            d += numBottles
            b += numBottles
            numBottles = 0
            numBottles = (b)//numExchange
            b = b%numExchange
        return d