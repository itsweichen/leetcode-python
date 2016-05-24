class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 5/23/2016
        # O(n^3) - 1282 ms [22%]

        n = len(nums)
        if n < 4:
            return []

        nums.sort()
        res = []

        iValue = jValue = pValue = sys.maxint

        for i in xrange(n-3):
            if nums[i] == iValue: # avoid duplicate quadruplets
                continue
            else:
                iValue = nums[i]
            for j in xrange(i+1, n-2):
                if nums[j] == jValue:
                    continue
                else:
                    jValue = nums[j]
                p = j + 1
                q = n - 1
                while p < q:
                    sum = iValue + jValue + nums[p] + nums[q]
                    if sum < target:
                        p += 1
                    elif sum > target: #1 not `else if` !!!
                        q -= 1
                    else:
                        if nums[p] != pValue: # or sums[q] = qValue
                            pValue = nums[p]
                            res.append([iValue, jValue, pValue, nums[q]]) #2 typo!
                        p, q = p + 1, q - 1
                pValue = sys.maxint #3 reinit!
            jValue = sys.maxint #3 reinit!

        return res
        
