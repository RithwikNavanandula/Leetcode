class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k = k-len(nums)
        p = deepcopy(nums)
        for i in range(len(p)):
            if i+k < len(nums):
                nums[i+k] = p[i]
            else:
                nums[i+k-len(nums)] = p[i]
        