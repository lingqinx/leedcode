class Solution(object):
    """
    def tranverse(self,substr,n):
        
        for i in range(len(nums)):
            v = nums[i:i+1]
        if len(nums) == 1:
            yield v
        else:
            rest = substr[:i] + nums[i+1:]
            for i in tranverse(rest, n-1):
                yield v+i
    def permute(self, nums):
        
        self.tranverse(nums,len(nums))
    """    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #当前字母加上前面部分排列和后面部分排列
        if len(nums) < 2: return [nums]
        return [ [a] + p for i, a in enumerate(nums) for p in self.permute(nums[:i] + nums[i+1:])]
