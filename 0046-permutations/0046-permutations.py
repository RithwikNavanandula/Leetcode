class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        k = [[nums[0]]]
        def per(p, i):
            ans = []
            for c in k:
                for j in range(len(c)):
                    b = deepcopy(c)
                    b.insert(j,i)
                    ans.append(b)
                c.append(i)
                ans.append(c)
            return ans
        for l in nums[1:]:
            k = per(k, l)
        return k
