class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 5/23/2016
        # O(nm) - m:length of longest string in strs
        # 60 ms [13%]

        n = len(strs)
        if n < 1:
            return ""

        cp = strs[0]
        for i in range(1, n):
            cur = strs[i]
            minLen = min(len(cp), len(cur))
            j = 0
            while j < minLen:
                if cp[j] == cur[j]:
                    j += 1
                else:
                    break
            cp = cp[:j]

        return cp
