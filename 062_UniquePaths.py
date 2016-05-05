class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # 5/4/2016
        # O(m*n) - 48ms [16%]

        # only use O(n) space

        if m == 0 or n == 0:
            return 0

        mat = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                prev = mat[j-1]
                mat[j] += prev

        return mat[n-1]


        """
        matrix = [1] * m
        for i in range(m):
            matrix[i] = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[m-1][n-1]
        """

        
