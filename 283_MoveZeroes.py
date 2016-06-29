class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 06/28/2016
        # 84 ms [46%]

        n = len(nums)

        i, j = 0, 0 # i: pointing to the place that needs to be replaced

        while j < n:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < n:
            nums[i] = 0
            i += 1
