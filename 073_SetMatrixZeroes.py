class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # 04/20/2016

        # hhh 哪有你想的辣么简单！-- 首先要理解题意！
        # 之后变的0不算！

        # 分别用两个dict来存，而非 append 到 list [(i,j)...] 来防止后面重复循环（设为0)
        # 184 ms [35%] -> 176 ms [61%]

        m = len(matrix)
        n = len(matrix[0])

        rows = {}
        cols = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for j in cols:
            for p in range(m):
                matrix[p][j] = 0

        for i in rows:
            for q in range(n):
                matrix[i][q] = 0
