class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0]*len(nums)
        for i in range(len(nums)):
            j = i
            if i+1 != len(nums) and nums[i] > nums[i+1]:
                while j+1 < len(nums) and nums[j] > nums[j+1]:
                    j +=1 
            elif i+1 != len(nums) and nums[i] < nums[i+1]:
                while j+1 < len(nums) and nums[j] < nums[j+1]:
                    j += 1
            l[i] = j-i+1
        return max(l)
                    