# 04/13/2016

# O(?) - 268ms [47%]
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if strs is None or len(strs) == 0:
            return strs

        res = []
        dict = {} # (string in lexi order, index of res)

        for i, str in enumerate(strs):
            lex = tuple(sorted(str))
            if lex in dict:
                # add to res[dict[lex]] in lex order
                index = dict[lex]
                for k in range(len(res[index])):
                    if str < res[index][k]:
                        res[index].insert(k, str)
                        break
                    if k == len(res[index]) - 1:
                        res[index].append(str)
            else:
                res.append([str])
                dict[lex] = len(res) - 1

        return res
