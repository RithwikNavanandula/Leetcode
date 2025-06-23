class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                p = i
                break
        return p