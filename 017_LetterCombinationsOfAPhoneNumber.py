# 03/29/2016

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # O(?), 56ms [5%]
        
        if digits == "" or digits is None:
            return []
        
        mapping = {}
        
        # add to a dict
        mapping["2"], mapping["3"] = "abc", "def"
        mapping["4"], mapping["5"], mapping["6"] = "ghi", "jkl", "mno"
        mapping["7"], mapping["8"], mapping["9"] = "pqrs", "tuv", "wxyz"
        mapping["0"] = ""
        
        res = []
        for digit in digits:
            temp = []
            if digit in mapping:
                for letter in mapping[digit]:
                    if len(res) == 0:
                        temp.append(letter)
                    else:
                        for item in res:
                            temp.append(item+letter)
                res = temp
            
        return res