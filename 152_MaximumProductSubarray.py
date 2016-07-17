class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 07/17/2016
        # 72 ms [30%]

        local_min, local_max, global_max = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            a, b = local_min * x, local_max * x
            local_min = min(x, a, b)
            local_max = max(x, a, b)
            global_max = max(global_max, local_max)

        return global_max
