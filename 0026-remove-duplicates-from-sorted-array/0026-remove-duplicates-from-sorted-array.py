class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = sorted(list(set(nums)))
        for i in range(len(k)):
            nums[i] = k[i]
        return len(k)
