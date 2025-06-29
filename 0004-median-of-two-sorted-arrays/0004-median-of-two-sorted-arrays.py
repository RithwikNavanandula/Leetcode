import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1 = sorted(nums1)
        if len(nums1)%2 == 0:
            mid = len(nums1) // 2
            return float(nums1[mid - 1] + nums1[mid]) / 2
        else:
            return nums1[int(ceil(len(nums1)/2))]