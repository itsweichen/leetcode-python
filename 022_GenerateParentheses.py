class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # 5/22/2016
        # 68 ms [12%]
        
        res = []
        self.solve(n, 0, "", res)

        return res

    def solve(self, n, nl, soFar, res):
        """
        n: remaining # of ()
        nl: how many unmatching ( added
        """

        if n <= 0 and nl == 0:
            res.append(soFar)

        # add (
        if n > 0:
            self.solve(n-1, nl+1, soFar+"(", res)

        # add )
        if nl > 0:
            self.solve(n, nl-1, soFar+")", res)
