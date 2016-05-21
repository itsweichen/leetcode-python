class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # 5/20/2016

        if num1 == "" or num2 == "":
            return ""

        m, n = len(num1), len(num2)
        num1R, num2R = num1[::-1], num2[::-1]
        resR = [0] * (m + n) # calculate in place!

        for i in xrange(m):
            for j in xrange(n):
                resR[i+j] += int(num1R[i]) * int(num2R[j])
                resR[i+j+1] += resR[i+j] / 10
                resR[i+j] = resR[i+j] % 10

        print resR

        res = ""
        j = 0
        for i in xrange(m+n-1, 0, -1):
            digit = resR[i]
            if digit != 0:
                for j in range(i, 0, -1):
                    res = res + str(resR[j])
                break

        res = res + str(resR[0]) # in case it's zero

        return res
