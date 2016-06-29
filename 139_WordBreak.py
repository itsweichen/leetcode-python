class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        # 06/27/2016

        # Time: O(n^2), Space: O(n)
        n = len(s)

        if n == 0: return True

        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i+1] = True
        return dp[-1]
        
