class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        """ 
        ret = []
        for num in digits:
            if not ret:
                for letter in dic[num]:
                    ret.append(letter )
                    print ret
            else:
                ret = [str+letter for letter in dic[num] for str in ret]
                print ret
        return ret
        
        """
        strings=[]
        if len(digits)<=1:
            for n in digits:
                return list(dic[n])
        for n in digits:
            if not strings:
                for s in dic[n]:
                    strings.append(s)  
            else:
                temp=[]
                for s in dic[n]:
                    print s
                    for string in strings:   
                        temp.append(string+s)  #存储字母相加后的list
                #print temp
                        #res.append(string+s)
                strings=temp #这个赋值在最外层
                        
        return strings
