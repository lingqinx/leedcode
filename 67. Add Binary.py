class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #bin()函数是整数转换成二进制字符串,int(a,2)二进制转十进制
        #http://www.pythontab.com/html/2013/pythonjichu_0102/86.html
        #int(a,2),bin(int(a,2)+int(b,2))
        return bin(int(a,2)+int(b,2))[2:]
