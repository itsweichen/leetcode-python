class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # 5/19/2016
        # 48 ms [21%]

        res = []

        if numRows <= 0:
            return res
        else:
            res.append([1]) # not append(1)

        for i in range(1, numRows):
            subLen = i + 1
            temp = [1]
            for j in range(1, subLen-1):
                temp.append(res[i-1][j-1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
        
        return res
