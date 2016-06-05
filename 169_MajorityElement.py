class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #1 use hash map to record # of times a certain item is visited
        # 62 ms [65%]
        
        visited = {}

        for item in nums:
            if item in visited:
                visited[item] += 1
            else:
                visited[item] = 1

        n = len(nums)
        for item in visited.keys():
            if visited[item] > n/2:
                return item
