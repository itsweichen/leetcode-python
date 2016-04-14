# 04/13/2016

# DP: O(n) - 56s [55%]
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return nums

        #l, r = 0, 0 # for outputing the corresponding array, unnecessary for this problem
        sum = nums[0]
        prevSum = nums[0] # max sum that ends with that value
        for i, num in enumerate(nums[1:]):
            if prevSum > 0:
                prevSum = prevSum + num
                if prevSum > sum:
                    #r = i
                    sum = prevSum
            else:
                prevSum = num
                if prevSum > sum:
                    #l, r = i, i
                    sum = prevSum

        return sum
