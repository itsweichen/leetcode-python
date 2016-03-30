# 03/29/2016

# O(?), 52ms [9%]
# initing res without judging each time doesn't improve much

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits == "" or digits is None:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
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