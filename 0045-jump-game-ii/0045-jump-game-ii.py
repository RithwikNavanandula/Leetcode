class Solution:
    def jump(self, nums):
        n = len(nums)
        maxReach = 0
        currReach = 0
        jumps = 0

        for i in range(n - 1):  # Note: range up to n-1 is fine
            maxReach = max(maxReach, i + nums[i])

            if i == currReach:
                jumps += 1
                currReach = maxReach

        return jumps
