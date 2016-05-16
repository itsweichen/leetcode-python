class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # 5/16/2016
        # 52 ms [31%]

        res = []

        self.grey(res, n)

        return res


    def grey(self, res, n):
        if n == 0:
            res.append(0) # n = 0, return [0] not []!
            return

        self.grey(res, n-1)

        new = 1 << n-1
        for i in range(len(res)-1, -1, -1):
            res.append(res[i]^new)
