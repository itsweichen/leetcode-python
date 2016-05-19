class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # make it shorter
        # 5/18/2016
        # 72 ms [20%]


        na = len(a)
        nb = len(b)
        pa = na - 1
        pb = nb - 1

        r = ""

        if na == 0:
            return b
        if nb == 0:
            return a

        carry = 0

        while pa >= 0 or pb >= 0:
            s = carry
            if pa >= 0:
                s += int(a[pa])
                pa -= 1
            if pb >= 0:
                s += int(b[pb])
                pb -= 1
            i = s % 2
            carry = s / 2
            r += str(i)

        if carry > 0:
            r += "1"

        return r[::-1]


    """
    def addBinary(self, a, b):

        na = len(a)
        nb = len(b)
        pa = na - 1
        pb = nb - 1

        r = ""

        if na == 0:
            return b
        if nb == 0:
            return a

        carry = 0

        while pa >= 0 and pb >= 0:
            s = int(a[pa]) + int(b[pb]) + carry
            i = s % 2
            #carry = s - i
            carry = s / 2
            r += str(i)
            pa -= 1
            pb -= 1

        while pa >= 0:
            s = int(a[pa]) + carry
            i = s % 2
            # carry = s - i
            carry = s / 2
            r += str(i)
            pa -= 1

        while pb >= 0:
            s = int(b[pb]) + carry
            i = s % 2
            #carry = s - i
            carry = s / 2
            r += str(i)
            pb -= 1

        if carry > 0:
            r += "1"

        return r[::-1]
    """
