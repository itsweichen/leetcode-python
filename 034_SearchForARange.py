class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 5/21/2016
        # 44 ms [76%]

        n = len(nums)

        if n == 0:
            return [-1, -1]

        ok = self.binarySearch(nums, 0, n-1, target)
        if ok != -1:
            l, r = ok - 1, ok + 1
            while l!=-1 and nums[l]==target  or r!=n and nums[r]==target: #!!!
                if nums[l] == target:
                    if l > -1 :
                        l -= 1
                if nums[r] == target:
                    if r < n:
                        r += 1
            return [l+1, r-1]

        else:
            return [-1, -1] # not return False

    def binarySearch(self, nums, l, h, target):
        if l > h:
            return -1

        mid = (h + l) / 2 # plus, not minus

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            ok = self.binarySearch(nums, l, mid-1, target)
        else:
            ok = self.binarySearch(nums, mid+1, h, target)

        if ok != -1: # ok might equal to 0!!!
            return ok
        else:
            return -1
