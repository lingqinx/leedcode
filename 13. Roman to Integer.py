class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        result=0
        i=1
        while i <len(s):
            if dicts[s[i-1]]>=dicts[s[i]]:
                result+=dicts[s[i-1]]
                i+=1
            else:
                result+=dicts[s[i]]-dicts[s[i-1]]
                i+=2
        if i<=len(s):   
            result+=dicts[s[-1]]
        return result
