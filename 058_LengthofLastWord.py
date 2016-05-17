class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 5/17/2016
        # 50 ms [22%]

        i = len(s) - 1
        res = 0

        while i >= 0:
            if s[i] != ' ':
                res += 1
            else:
                if res != 0:
                    break
            i -= 1

        return res

"""
class Solution(object):
    def lengthOfLastWord(self, s):

        # 52 ms [13%]

        j = len(s) - 1

        if j == -1:
            return 0

        if s[-1] == ' ':
            for i in xrange(len(s) - 1, -1, -1):
                if s[i] == ' ':
                    if i == 0:
                        return 0
                    continue
                else:
                    j = i
                    break


        for i in xrange(j, -1, -1):
            if s[i] == ' ':
                return j-(i+1)+1

        return j+1

"""
