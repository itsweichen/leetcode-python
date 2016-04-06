class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 05/04/2016
        # O(n) - 44ms [27%]

        stack = []
        mapping = {'(': ')', '{':'}', '[':']'}

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if len(stack) == 0 or mapping[stack.pop()] != char:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
