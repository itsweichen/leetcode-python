# 04/13/2016

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 神奇的Greedy
        # O(n) - 56m [65%]
        # https://leetcode.com/articles/jump-game/

        length = len(nums)
        i = length - 1
        lastPos =  i

        while(i>0):
            i -= 1
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0

        """ DP: Time Limit Exceeded - O(n^2)

        if nums is None or len(nums) == 0:
            return False

        length = len(nums)
        i = length - 1
        m = [False] * length
        m[length-1] = True

        while(i>0):
            i -= 1

            if nums[i] >= length - i - 1:
                m[i] = True
                continue

            for j in xrange(i+1, i+nums[i]+1):
                if m[j] == True:
                    m[i] = True
                    break # be careful of nested loop

        return m[0]
        """

        """ Recursion: [Memory Limit Exceeded]
        # what if [1, 1, 1, ..., 1]?

        if nums is None or len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        for i in range(1, nums[0] + 1 if nums[0] + 1 <= len(nums) else len(nums)):
            return self.canJump(nums[i:]) #!!!

        return False #!!!
        """
