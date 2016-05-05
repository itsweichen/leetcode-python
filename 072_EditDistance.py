class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # 5/4/2016
        # O(mn) - 268ms [77%]

        # 4 CAVEATS!

        if len(word1) == 0:
            return len(word2)

        if len(word2) == 0:
            return len(word1)

        len1 = len(word1) + 1
        len2 = len(word2) + 1

        # init the matrix
        s = [0] * len1
        for i in xrange(len(s)):
            s[i] = [0] * len2

        # base case
        for i in xrange(len1):
            s[i][0] = i

        for j in xrange(len2):
            s[0][j] = j

        # fill the table
        for i in xrange(1, len1):
            for j in xrange(1, len2):
                if word1[i-1] == word2[j-1]:
                    s[i][j] = s[i-1][j-1]
                else:
                    s[i][j] = min(s[i-1][j-1], s[i-1][j], s[i][j-1]) + 1

        return s[len1 - 1][len2 - 1]
        
