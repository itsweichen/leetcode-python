class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 06/30/2016
        # Time: O(n)*2, Space: O(n)

        n, m = len(s), len(t)

        if n != m:
            return False

        d = {}

        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1

        for i in range(m):
            if t[i] not in d:
                return False
            else:
                d[t[i]] -= 1
                if d[t[i]] < 0:
                    return False

        return True
