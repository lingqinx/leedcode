class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        else:
            d=n*[0]

            d[0]=1
            d[1]=2
            i=2
            while i <n:
                d[i]=d[i-1]+d[i-2]
                i+=1
            return d[i-1]
