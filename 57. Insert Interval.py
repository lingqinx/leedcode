# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right=[],[]
        s = newInterval.start
        e= newInterval.end
        left = [i for i in intervals if i.end<s]
        right = [i for i in intervals if i.start>e]
        if left + right != intervals:
            s= min(intervals[len(left)].start, s)
            e= max(intervals[~len(right)].end,e)
        return left+ [Interval(s,e)]+right
