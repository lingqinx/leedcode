class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0;
        k=0;
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1 
                nums[k] = nums[i]

        return k+1
