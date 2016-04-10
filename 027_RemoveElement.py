class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if nums is None or len(nums) == 0:
            return 0

        newIndex = 0

        for i, num in enumerate(nums):
            if num != val:
                nums[newIndex] = num
                newIndex += 1

        return newIndex
