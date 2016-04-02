# backtracking

class Solution(object):
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # O(?) - 80ms [49%]

        if nums is None:
            return [[]]
        
        if len(nums) < 2:
            return [nums]
        
        # use the result as an argument (problems of using global var in leetcode)
        res = []
        self.helper([], nums, res)
        
        return res
        
    def helper(self, soFar, rest, res):
        if len(rest) == 0:
            res.append(soFar)
        else:
            for i, num in enumerate(rest):
                remaining = rest[:i] + rest[i+1:]
                self.helper(soFar + [num], remaining, res)
            
    