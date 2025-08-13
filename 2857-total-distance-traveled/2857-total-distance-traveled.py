class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        p = 0
        mainTank -=5
        p+=50    
        while mainTank > -1:
            if additionalTank > 0:
                mainTank+=1
                additionalTank-=1
            mainTank -=5
            p+=50
        p+=mainTank*10
        return p