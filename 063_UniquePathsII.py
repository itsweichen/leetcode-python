class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # 5/4/2016
        # 60 ms [8%]

        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        mat = [0] * m

        for i in range(m):
            mat[i] = [0] * n

        # base case
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                mat[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                mat[0][j] = 1
            else:
                break
        print m, n
        for i in range(1, m): # 注意从1开始！
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]

        return mat[m-1][n-1]
