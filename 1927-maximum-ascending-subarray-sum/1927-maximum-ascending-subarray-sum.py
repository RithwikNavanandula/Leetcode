class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0]*len(nums)
        for i in range(len(nums)):
            j = i
            sums = nums[i] 
            if i+1 != len(nums) and nums[i] < nums[i+1]:
                while j+1 < len(nums) and nums[j] < nums[j+1]:
                    j += 1
                    sums += nums[j]
            l[i] = sums
        return max(l)
