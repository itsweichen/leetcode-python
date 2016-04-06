class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 04/05/2016
        # O(n^2) - 320ms (28%)

        if nums is None:
            return []

        res = {}
        nums.sort() # directly sort the list
                    # (instead of returning a sorted list, return None)

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    pro = (nums[i], nums[left], nums[right])
                    if pro not in res:
                        res[pro] = '0'
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(res) # turn dict -> list (adding only keys to the list)
