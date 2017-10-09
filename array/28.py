#!/usr/bin/python
#coding=utf-8
#在haystack（数组？）字符串也是数组
import math

class Solution(object):
    def removeDuplicates(self, haystack, needle):

        k=0;
        for k in range(0,len(haystack)-len(needle)+1):
            if haystack[k:k+len(needle)] == needle:
              return k
        return -1

if __name__ == "__main__":
    so = Solution()
    haystack = ""
    needle = ""
    print so.removeDuplicates(haystack, needle)
	
