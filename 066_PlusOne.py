class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # 5/18/2016
        # 52s [18%]

        n = len(digits)

        if n == 0:
            return [1] # what should I return here?

        for i in range(n-1, -1, -1): #2 out of range: range 如何设置 = =
            temp = 1 + digits[i]
            if temp < 10: #优化：少加一次
                digits[i] = temp
                return digits
            else:
                digits[i] = 0
        digits = [1] + digits
        return digits

        #1 想清楚到底怎么存！The digits are stored such that the most significant digit is at the head of the list.
