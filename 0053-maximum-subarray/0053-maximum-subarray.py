class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = -float('inf')
        sum = 0
        for i in nums:
            sum += i
            ma = max(sum, ma)
            if sum < 0:
                sum = 0
        return ma
