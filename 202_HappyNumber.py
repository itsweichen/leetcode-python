class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 07/01/2016
        # 64 ms [50%]

        d = {}
        cur = n
        while cur != 1 and cur not in d:
            d[cur] = 0
            prev = cur
            cur = 0
            while prev > 0:
                digit = prev % 10
                prev /= 10
                cur += digit**2
        return cur == 1
