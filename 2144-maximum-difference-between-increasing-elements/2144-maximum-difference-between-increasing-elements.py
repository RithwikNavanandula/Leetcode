class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j]-nums[i] > maxi and nums[j]-nums[i] != 0:
                    maxi = nums[j]-nums[i]
        return maxi
