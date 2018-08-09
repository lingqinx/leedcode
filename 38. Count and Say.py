class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=['1','11']
        for j in range(2,n):
            res.append(self.count(res[j-1]))
        return res[n-1]  
    def count(self, s):
        res=''
        i=0
        while i<len(s):
            i+=1
            #print i,s
            count=1
            while i<len(s) and s[i]==s[i-1]:
                i+=1
                count+=1
            res+=str(count)+s[i-1]
            #print res,i,count
        return res
