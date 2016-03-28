# 03/24/2016

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # [25%]
        # ref[1]: https://github.com/kamyu104/LeetCode/blob/master/Python/zigzag-conversion.py
        # ref[2]: http://blog.unieagle.net/2012/11/08/leetcode%E9%A2%98%E7%9B%AE%EF%BC%9Azigzag-conversion/
        
        if s is None or len(s) == 0:
            return ""
            
        if numRows == 1:
            return s
        
        step = numRows + numRows - 2
        # any difference in running time for using range/xrange?
        zigzag = ""
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
                    
        return zigzag