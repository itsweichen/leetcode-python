class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 5/24/2016
        # 76 ms [13%]

        n = len(nums)
        if n <= 1:
            return
        if n == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    return
            for j in xrange(i+1, n):
                nums[j-1], nums[j] = nums[j], nums[j-1]
