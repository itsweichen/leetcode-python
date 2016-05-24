class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # 5/24/2016
        # 68 ms [18%]

        if divisor == 0:
            return 0
        if dividend == 0:
            return 0

        isMinus = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            isMinus = True

        divisor, dividend = abs(divisor), abs(dividend)

        i = 0
        curRes = 0
        factor = 0
        while curRes <= dividend: # <= not <
            curRes += divisor << i # 搞清楚左移还是右移！
            # factor = factor + 1 << i # wrong!
            factor = factor + (1 << i) # + has higher priority!
            i += 1

        i -= 1
        curRes -= divisor << i
        factor = factor - (1 << i)

        for j in xrange(i-1, -1, -1):
            temp = curRes + (divisor << j)
            if temp <= dividend:
                factor = factor + (1 << j)
                curRes = temp

        # how do we know if it's overflow??
        factor = -factor if isMinus else factor
        if factor < -2147483648 or factor > 2147483648 - 1: # 2**31-1
            factor = 2147483647

        return factor
