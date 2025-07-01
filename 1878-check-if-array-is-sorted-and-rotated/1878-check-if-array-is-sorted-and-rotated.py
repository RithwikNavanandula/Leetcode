class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == p[0]:
                v = nums[i:] + nums[:i]
                if v == p:
                    return True
        return False

        