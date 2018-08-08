class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        j=len(x)-1
        i=0
        while j>i:
            if x[i]==x[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        
