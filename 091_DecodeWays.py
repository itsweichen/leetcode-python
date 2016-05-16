class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 5/16/2016
        # 56 ms [46%]
        
        if len(s) == 0:
            return 0

        dp = [0] * len(s)

        if s[0] != '0':
            dp[0] = 1

        cases = {}
        for i in range(1,27):
            cases[str(i)] = '0'

        if len(s) > 1:
            if s[1] == '0':
                dp[1] = dp[0] if s[0:2] in cases else 0
            else:
                if dp[0] == 0:
                    dp[1] = 0
                else:
                    dp[1] = 2 if s[0:2] in cases else 1

        for i in xrange(2, len(s)):
            if s[i] == '0':
                if s[i-1:i+1] in cases:
                    dp[i] += dp[i-2]
                else:
                    dp[i] = 0
            else:
                dp[i] += dp[i-1]
                if s[i-1:i+1] in cases:
                    dp[i] += dp[i-2]
