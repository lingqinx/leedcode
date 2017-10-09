#!/usr/bin/python
#coding=utf-8
#此方法改变了顺序，但貌似没改变nums本身
import math

class Solution(object):
  def rotate(self, nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
    if k <= len(nums):
      temp = []
      for i in range(0,len(nums)):
        temp.append(nums[i-k]) 
      nums = temp
      print nums
    #k大于长度的也要rotate,若大于则是取模继续rotate
      """
    if k <= len(nums):
      k=k%len(nums)
      nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k] #不能是直接nums[k]
#    else:

#      nums[::] = nums[::-1]
    


if __name__ == "__main__":
  so = Solution()
  nums = [1,2]
  so.rotate(nums,1)
  print nums
