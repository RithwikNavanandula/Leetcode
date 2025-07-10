class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        res = nums[-1]-nums[0]
        for i in range(len(nums)-1):
            b = max(nums[-1], nums[i]+2*k)
            s = min(nums[i+1], nums[0]+2*k)
            res = min(res, b-s)
        return res