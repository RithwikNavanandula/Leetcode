class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = {}
        k = []
        nums.sort()
        for i in nums:
            if i not in p:
                p[i] = 1
            else:
                p[i]+=1
            
            if p[i] > len(nums)//3:
                if i not in k : k.append(i)
                if len(k) == 2:
                    return list(set(k))
        return list(set(k))