class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 06/28/2016

        # 68 ms [32%]
        #1 Space:O(n), Time:O(n)
        n = len(nums)
        d = {}
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 0
            else:
                return True
        return False

        #2 Sort first - Space:O(n), Time:O(nlogn)
