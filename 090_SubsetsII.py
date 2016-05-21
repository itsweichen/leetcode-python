class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 5/20/2016
        # 76 ms [39%]

        res = []
        dup = {}
        nums.sort()
        self.solve([], nums, res, dup)

        return res

    def solve(self, soFar, rest, res, dup):
        if rest == []:
            if tuple(soFar) not in dup:
                dup[tuple(soFar)] = 0
                res.append(soFar)
        else:
            self.solve(soFar + [rest[0]], rest[1:], res, dup)
            self.solve(soFar, rest[1:], res, dup)
