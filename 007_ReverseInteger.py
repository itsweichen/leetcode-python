class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # 06/21/2016

        res = 0
        neg = -1 if x < 0 else 1
        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x /= 10
        res *= neg
        return res if res <= 2147483648 - 1 and res >= -2147483648 else 0
