class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 07/17/2016
        # 120 ms [67%]

        n = len(s)
        loc, vowels_list  = set(), []
        vowels_set = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]) # upper letter!

        for i in range(n):
            if s[i] in vowels_set:
                loc.add(i)
                vowels_list.append(s[i])

        res = [""] * n
        k = 0
        for i in xrange(n-1, -1, -1):
            if i in loc:
                res[i] = vowels_list[k]
                k += 1
            else:
                res[i] = s[i]

        return "".join(res)
