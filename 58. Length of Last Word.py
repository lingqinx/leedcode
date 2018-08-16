class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        else:           
            k=0
            for i in s:
                if i == ' ' and :
                    k=0
                if i != ' ':
                    k+=1
            return k
