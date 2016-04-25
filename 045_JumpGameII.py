class Solution(object):

    # 04/24/2016
    # O(n) - 68 ms [46%]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        reach = 0
        lastReach = 0

        for i, num in enumerate(nums):
            if lastReach < i:
                step += 1
                lastReach = reach

            reach = max(reach, num+i)

        return step
