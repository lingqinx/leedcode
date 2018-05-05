# encoding: UTF-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        else:
            intervals = sorted(intervals,key=lambda i: i.start)#先排序，有序处理简单
            j=1
            while j<len(intervals):
# if,和循环的先后使用，几次都栽在这
                if intervals[j].start <= intervals[j-1].end:
                    intervals[j].start=min(intervals[j-1].start,intervals[j].start)
                    intervals[j].end=max(intervals[j-1].end,intervals[j].end)
                    intervals[j-1:]=intervals[j:]
                else: 
                    j=j+1

            return intervals