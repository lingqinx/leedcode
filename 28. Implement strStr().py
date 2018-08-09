class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """
        it should be 0 because the question not require -1 when 0 haystack
        if not haystack:
            return -1;
        """
        k=0;
        for k in range(0,len(haystack)-len(needle)+1):
            if haystack[k:k+len(needle)] == needle:
                return k
        return -1
