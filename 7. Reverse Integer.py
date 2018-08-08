class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        oper = 0
        if x > 0:
            oper = 1
            reverse=int(str(x)[::-1])
            
        if x < 0:
            oper = -1
            reverse = int(str(x)[1::-1])
        reverse = int(`oper*x`[::-1])
