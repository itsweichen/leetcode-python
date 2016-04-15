
# 04/14/2016
# 116 [10%]

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board is None or len(board) % 3 != 0:
            return False

        checkDict = {}
        for i in range(1, 10):
            checkDict[str(i)] = 0

        n = len(board) # n x n

        # check rows
        for i in range(n):
            dictRow = dict.copy(checkDict)
            for j in range(n):
                if not self.checkItem(dictRow, board[i][j]):
                    return False

        # check colums
        for j in range(n):
            dictCol = dict.copy(checkDict)
            for i in range(n):
                if not self.checkItem(dictCol, board[i][j]):
                    return False

        # check sub box
        n_sub = n / 3
        for i in range(n_sub):
            for j in range(n_sub):
                dictSub = dict.copy(checkDict)
                for m in range(3):
                    for n in range(3):
                        item = board[i*3+m][j*3+n]
                        if not self.checkItem(dictSub, item):
                            return False

        return True

    def checkItem(self, dict, item):
        if item == '.':
            return True
        if item in dict and dict[item] == 0:
            dict[item] = 1
        else:
            return False
        return True
