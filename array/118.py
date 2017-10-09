#!/usr/bin/python
#coding=utf-8

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
       """
        if numRows == 0:
       		return []
       	else:
       		List = [[1]]
        	for x in range(1,numRows):
#list 添加元素append(),extend(),insert(),+,这里直接+,建了新list,消耗内存 List = List + 新的一行
        		List += [map(lambda x,y: x+y, List[-1] + [0], [0] + List[-1])]
        	return List[:numRows]

    	

if __name__ == "__main__":
	so = Solution()
	print so.generate(5)