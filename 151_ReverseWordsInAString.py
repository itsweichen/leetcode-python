class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        j = len(s) - 1
        if j <= -1:
            return ''

        while j > -1 and s[j] == ' ':
            j -= 1

        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        words = []
        word = ''
        for k in xrange(i, j+1):
            cur = s[k]
            if cur == ' ' and word != '':
                words.append(word)
                word = ''
            if cur != ' ':
                word += cur

        # should append the last one!
        if word != '':
            words.append(word)

        res = ''
        for k in xrange(len(words)-1, -1, -1):
            res += words[k] + ' '

        return res[:-1]
