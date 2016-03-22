# 03/21/2016

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #1 O(n^2)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if ( nums[i] + nums[j]==target ):
                    return [i, j]
        """

        #2 Use Hash Table! - O(n) [50%]
        lookups = {}
        for i, num in enumerate(nums):
            if target - num in lookups:
                return [lookups[target-num], i]
            lookups[num] = i