class Solution(object):

    """
    # more elegant way
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current
        return current
    """

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 5/17/2016

        if n <= 1:
            return 1

        if n == 2:
            return 2

        f, g = 1, 2
        step = 0
        for i in xrange(3, n+1):
            step = f + g
            f = g
            g = step

        return step
