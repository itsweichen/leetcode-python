class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 07/15/2016

        mapping = {}
        mapped = set()

        for i in range(len(s)):
            cur = s[i]
            if cur in mapping:
                if mapping[cur] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] not in mapped: #!!!
                    mapping[cur] = t[i]
                    mapped.add(t[i])
                else:
                    return False

        return True
