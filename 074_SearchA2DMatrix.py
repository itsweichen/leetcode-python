class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # 5/4/2016
        # BinarySearch

        # 54 ms [28%]

        if target is None or matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])

        return self.binarySearch(target, matrix, m, n, 0, m * n - 1)

    def binarySearch(self, target, matrix, m, n, l, h):
        if l > h:
            return False

        mid = (l + h) / 2
        i = mid / n
        j = mid % n

        if matrix[i][j] == target:
            return True
        if matrix[i][j] < target:
            return self.binarySearch(target, matrix, m, n, mid+1, h)
        else:
            return self.binarySearch(target, matrix, m, n, l, mid-1)


        
