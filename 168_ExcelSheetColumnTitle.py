class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        # 06/29/2016

        k = 26
        res = ""
        while n > 0:
            r = n % k
            n = n / k
            if r == 0:
                res = "Z" + res
                n -= 1
            else:
                res = chr(r - 1 + ord("A")) + res

        return res
