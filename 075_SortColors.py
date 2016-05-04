class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 5/3/2016
        # \theta(2n), 48ms [37%]

        helper = [0, 1] + nums
        p, q = 0, 1

        for i in range(len(nums)):
            i += 2
            if helper[i] == 0:
                helper.insert(p, helper.pop(i))
                p, q = p+1, q+1
            elif helper[i] == 1:
                helper.insert(q, helper.pop(i))
                q += 1
            else:
                continue

        helper.pop(q)
        helper.pop(p) # first pop p, otherwise the index will move!
        #nums = helper # this won't work! you have to modify nums in-place!
        # use id(object) to see if it references the same object
        for i in range(len(nums)):
            nums[i] = helper[i]
