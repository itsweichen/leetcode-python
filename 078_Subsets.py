class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 04/27/2016
        # 56 ms [56%]

        if nums is None or len(nums) == 0:
            return [[]]

        res = []
        nums.sort() # Elements in a subset must be in non-descending order.
        self.helper([], nums, res)
        return res


    def helper(self, soFar, rest, res):
        if len(rest) == 0:
            res.append(soFar)
        else:
            self.helper(soFar + [rest[0]], rest[1:], res)
            self.helper(soFar, rest[1:], res)
