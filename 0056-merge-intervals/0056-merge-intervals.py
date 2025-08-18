class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda a:a[0])
        res = [intervals[0]]
        for i in intervals[1:]:
          for j in res:
            if j[0] <= i[0] <= j[1]:
              j[1] = max(i[1], j[1])
              break
          else:
            res.append(i)
        return res