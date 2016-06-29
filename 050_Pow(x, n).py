class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # 06/27/2016

        if n == 0: return 1

        res = 1
        absN = abs(n)
        while absN > 0:
            if absN & 1 == 1:
                res *= x
            absN >>= 1
            x *= x

        return res if n > 0 else 1/res
