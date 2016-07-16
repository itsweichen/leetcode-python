class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # 5/20/2016
        # 68 ms [20%]
        # function call: 204 ms

        if m == 0: return 0
        if n == 0: return -1

        for i in range(n):
            if haystack[i] == needle[0]:
                # don't make it a function call here.
                ok = True
                if n - i >= m:
                    for j in range(m):
                        if haystack[i+j] != needle[j]:
                            ok = False
                            break
                else:
                    ok = False #!!!
                if ok:
                    return i
        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0
        if haystack == "":
            return -1

        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i] == needle[0]:
                ok = self.checkNeedle(haystack[i:], needle, m)
                if ok:
                    return i
        return -1

    def checkNeedle(self, sp, needle, m):
        if len(sp) >= m:
            for j in range(m):
                if sp[j] != needle[j]:
                    return False
            return True
        else:
            return False
