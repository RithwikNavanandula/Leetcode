class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        for i in nums:
            if i == 1:
                l+=1
                res = max(res,l)
            else:
                l = 0
        return res           