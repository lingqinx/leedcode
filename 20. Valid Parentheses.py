class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=[]
        dic={'(':')','[':']','{':'}'}
        for i in s:
            if i in dic.keys():
                res.append(dic[i])
            elif i in dic.values():
                if res==[]:
                    res.append(i)
                elif res.pop()!=i:
                    return False

        if res:
            return False
        else:
            return True
