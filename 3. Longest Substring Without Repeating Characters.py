class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int        
        #一个例子超时,结果正确
        maxi=0
        for i in range(len(s)-maxi):
            k=0
            while k<len(s)-i:
                if s[i+k] not in s[i:i+k]:
                    #print i+k,s[i+k],s[i:i+k]
                    k+=1
                    maxi=max(maxi,k)    
                else:
                    break
                
        return maxi
        """
        if len(s)==0:
            return 0
        max_len=1
        k=0
        for i in range(1,len(s)):
            if s[i] not in s[k:i]:
                max_len=max(max_len,i-k+1)
            else:
                k+=s[k:i].index(s[i])+1
        return max_len
