import math

class Solution(object):
    def removeDuplicates(self, nums, val):
      if not nums:
        return 0;
      k=0;
      for i in range(0, len(nums)):
      	if nums[i] != val:
          nums[k] = nums[i]
          k += 1 
     
      return k

if __name__ == "__main__":
	so = Solution()
	nums = [1,2,3,4,5,1,2,3,4,5,6,1,2]
	print so.removeDuplicates(nums,3)
	print nums
