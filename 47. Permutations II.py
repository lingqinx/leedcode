class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2: return [nums]
        res=[]
        for i, a in enumerate(nums):
            for p in self.permuteUnique(nums[:i] + nums[i+1:]):
                s=[a] + p 
                #print s
                if s not in res:
                    res.append(s)
        
        return res
