class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):


        # choose the largest number first to place in the higher digit
        # use string to compare? [lex order]

        nums_str = [str(x) for x in nums]
        nums_str.sort(cmp=lambda x, y: cmp(y+x, x+y)) # deprecated in Python3
        res = "".join(nums_str)
        return res.lstrip("0") or "0"
