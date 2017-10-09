#!/usr/bin/python
#coding=utf-8

class Solution(object):
    def genRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
       """

     		List = [[1]]
      	for x in range(1,rowIndex+1):
      		List += [map(lambda x,y: x+y, List[-1] + [0], [0] + List[-1])]
      	return List[rowIndex]

    	

if __name__ == "__main__":
	so = Solution()
	print so.genRow(3)