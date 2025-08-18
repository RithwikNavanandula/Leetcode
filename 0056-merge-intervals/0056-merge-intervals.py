class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda a:a[0])
        res = [intervals[0]]
        for i in intervals[1:]:
          if res[-1][0] <= i[0] <= res[-1][1]:
            res[-1][1] = max(i[1], res[-1][1])
          else:
            res.append(i)
        return res