class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res=''
        for i in range(len(strs[0])):
            j=1
            while j<len(strs) and i<len(strs[j]):
                #print strs[0][i],strs[j][i]
                if strs[0][i]==strs[j][i]:
                    j+=1
                else:
                    return res
            if j==len(strs):
                res+=strs[0][i]
        return res
