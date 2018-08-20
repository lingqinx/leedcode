class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=[]
        num=0
        for i in range(len(digits)):
            num=10*num+digits[i]
        num+=1
        while num/10 > 0:
            result.append(num%10)
            num=num/10
        result.append(num%10)
        return result[::-1]
