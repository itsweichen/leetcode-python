# 好吧，其实应该直接对数字进行处理而不是转成string的 = =

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # 05/04/2016
        # O(n) - 252 ms [86%]

        # 直接reverse再比较就好，如何考虑 overflow 的情况？

        if x < 0:
            return False

        xcopy, reverse = x, 0

        while xcopy:
            reverse = 10 * reverse + xcopy % 10
            xcopy /= 10

        return x == reverse

#################

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # 05/04/2016
        # O(n) - 248 ms [90%]

        # what if x < 0 ?

        xstr = str(x)
        left = 0
        right = len(xstr) - 1
        while left < right:
            if xstr[left] == xstr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
