class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        right=len(s)-1
        while right>left:
            if s[left]==s[right]:
                left+=1
                right-=1
                
            else:
                self.longestPalindrome(s[left+1:right]) 
                self.longestPalindrome(s[left:right-1])
                
