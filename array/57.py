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
 #未解决合并问题TypeError: unsupported operand type(s) for +: 'Interval' and 'list'
 不清楚怎么插入这个newInterval   解决了插入Interval :[Interval(s,e)]   
        if len(intervals)==0:
            return newInterval
        for i in range(1,len(intervals)):            
            if intervals[i].start > newInterval.end and intervals[i-1].end<newInterval.start:
                s=newInterval.start
                e=newInterval.end
                intervals=intervals[i:]+[Interval(s,e)]+intervals[i+1:]
                return intervals
            if newInterval.start > intervals[i-1].start:
                if newInterval.end < intervals[i].start:
                    intervals[i-1].end=max(newInterval.end,intervals[i-1].end)
                    intervals[i-1:]=intervals[i:]
                else:                    
                    intervals[i].end=max(intervals[i].end,newInterval.end)
                    intervals[i-1:]=intervals[i:]          
            else:
                i=i+1
            return intervals
            """
#下面每一步都几乎犯错，之前思路行得通，只是条件判断静不下来写。。。
        left, right=[],[]
        s = newInterval.start#后面变量太长可考虑用短的表示
        e= newInterval.end
        left = [i for i in intervals if i.end<s]#别漏了for前的i,指给left赋了i
        right = [i for i in intervals if i.start>e]#仍是i，除去left的
        if left + right != intervals:#left,right都是Interval，一堆list
            s= min(intervals[len(left)].start, s)
            e= max(intervals[~len(right)].end,e)#~len(right),指从中间的几个Interval里取最大的那个
        return left+ [Interval(s,e)]+right #Interval是个方法，里面包含不止一个list，是从s到e的可多个Interval
                
        