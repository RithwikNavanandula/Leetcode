class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        on = []
        for i in nums:
            if i not in on:
                on.append(i)
            else:
                on.remove(i)
        return on[0]