class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 5/26/2016
        # 96 ms

        """
        Time Limit Exceeded
        n = len(s)
        res = ""
        for i in xrange(n-1, -1, -1):
            res += s[i]
        return res
        """

        n = len(s)
        start, end = 0, n-1 # cannot use s!
        res = list(s) # string -> list
        while start < end:
            res[start], res[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(res) # list -> string
