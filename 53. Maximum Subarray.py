class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        sum = 0
        for n in nums:
            sum += n
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max
