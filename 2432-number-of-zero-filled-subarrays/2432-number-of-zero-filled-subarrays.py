class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        n = len(nums)
        k = []
        while i < n:
            if nums[i] == 0:
                j = 0
                while i < n and nums[i] == 0 :
                    i+=1
                    j +=1
                k.append(j)
            else:
                i+=1
        m = 0
        for i in k:
            m+= i*(i+1)/2
        return m