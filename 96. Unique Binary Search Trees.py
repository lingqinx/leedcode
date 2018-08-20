class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
        res=[1,1]
        while len(res)<=n:
            sum=0
            for i in range(len(res)):
                sum+=res[i]*res[len(res)-i-1]
                #print len(res)-i-1,sum,   res[i],res[len(res)-i-1]
            res.append(sum)
        return res[n]
