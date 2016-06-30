class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 06/29/2016
        # 96 ms [60%]

        i, j = 0, len(s) - 1
        s = s.lower()

        while i < j:
            if not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                continue

            if not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True
