
# 06/04/2016
# O(n^2) - 172ms [47%]

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums is None or len(nums) < 3:
            return

        nums.sort()

        # init
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target - result) > abs(target - sum):
                    result = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return target

        return result
