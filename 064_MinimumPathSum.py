class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 04/20/2016
        # Dynamic programming

        # O(n^2) - 64 ms [70%]

        # Base case
        m = len(grid)
        n = len(grid[0])

        if m == 0 or n == 0:
            return 0

        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        # inductive
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

        return grid[m-1][n-1]
