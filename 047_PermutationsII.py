# 04/13/2016

# O(?) - 128ms [46%]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if nums is None or len(nums) == 0:
            return nums

        res = []
        self.helper([], nums, res)
        return res


    def helper(self, soFar, rest, res):
        if len(rest) == 0:
            return res.append(soFar)
        else:
            dict = {}
            for i, num in enumerate(rest):
                if num not in dict:
                    remaining = rest[:i] + rest[i+1:]
                    dict[num] = 0
                    self.helper(soFar + [num], remaining, res)
