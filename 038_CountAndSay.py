class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # 06/24/2016

        if n == 1: return "1"

        res = "1"

        for i in range(n-1):
            res += " "
            cnt = 1
            tmp = ""

            for j in range(1, len(res)):
                if res[j-1] == res[j]:
                    cnt += 1
                else:
                    tmp += str(cnt) + res[j-1]
                    cnt = 1 #!

            res = tmp

        return res
