class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 58 ms [50%]

        count = 0
        NUM_BITS = 32
        for i in range(NUM_BITS):
            cur = 1 << i
            if cur & n == cur:
                count += 1
        return count
