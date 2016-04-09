class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 04/08/2016
        # O(n) - 96ms [50%]
        # 注意看题！还需要修改nums

        if nums is None or len(nums) == 0:
            return 0

        prev = nums[0]
        newLength = 1

        for i in range(1, len(nums)):
            curItem = nums[i]
            if curItem != prev:
                nums[newLength] = curItem
                newLength += 1
                prev = curItem

        return newLength
