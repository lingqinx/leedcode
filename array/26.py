#!/usr/bin/python
#coding=utf-8
import math

class Solution(object):
    def removeDuplicates(self, nums):
      if not nums:
        return 0
      k=0;
      for i in range(1, len(nums)):
      	if nums[i] != nums[k]:
      		k += 1 
      		#k +=1 before nums[k] = nums[i] because num[k+1] replaced by new value
      		#python does not support ++,not need ;
      		nums[k] = nums[i]
     
      return k+1

if __name__ == "__main__":
	so = Solution()
	nums = [1,1,1,2,2,3]
	print so.removeDuplicates(nums)
	print nums
