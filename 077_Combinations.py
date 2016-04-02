class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # O(?) - 80ms [50%]

        res = []
        nums = range(1, n+1)
        self.helper(res, k, [], nums)
        
        return res
        
    def helper(self, res, k, soFar, rest):
        if len(soFar) == k:
            res.append(soFar)
        else:
            for i, num in enumerate(rest):
                remaining = rest[i+1:]
                self.helper(res, k, soFar + [num], remaining)
            