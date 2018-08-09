class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def backtrace(s='',left=0,right=0):
            if len(s)== 2*n :
                res.append(s)
                return
            if left<n:
                backtrace(s+'(',left+1,right)
            if right<left:
                backtrace(s+')',left,right+1)
        backtrace()       
        return res
