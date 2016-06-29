class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 06/26/2016

        #s[i]: max ends with i

        n = len(nums)

        if n == 0: return 0
        if n == 1 or n == 2: return max(nums)

        s = [0] * 3

        # base case
        s[0] = nums[0]
        s[1] = nums[1]
        s[2] = nums[2] + nums[0]

        maxNum = max(s)

        # recursive relation
        for i in range(3, n):
            s += [max(s[1]+nums[i], s.pop(0)+nums[i])]
            maxNum = max(s[2], maxNum)

        # final result
        return maxNum
