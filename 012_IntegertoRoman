class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # 05/04/2016
        # O(n) - 144ms [27%]

        # RomanChart: http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
        # Ref: https://github.com/kamyu104/LeetCode/blob/master/Python/integer-to-roman.py

        mapping = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
            40: "XL", 50: "L", 90: "XC", 100: "C",
            400: "CD", 500: "D", 900: "CM", 1000: "M"
        }

        keys = sorted(mapping.keys())
        res = ""

        for key in reversed(keys): # 从大到小iterate那个key list （而不是输入本身）
            while num / key > 0:
                num -= key
                res += mapping[key]

        return res
