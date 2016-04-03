# sol_1 - 03/29/2016 - intuitive(iteration)
# sol_2 - 04/02/2016 - recursion

class Solution_1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        # O(?), 52ms [9%]
        # initing res without judging each time doesn't improve much

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

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # O(?), 44 ms [36%]


        if len(digits) == 0:
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
        
        result = []
        
        self.helper("", digits, result, mapping)
        
        return result
        
        
    def helper(self, soFar, rest, result, mapping):
        # base case
        if len(rest) == 0:
            result.append(soFar)
            
        else:
            curDigit = rest[0]
            
            if curDigit in mapping:
                for letter in mapping[curDigit]:
                    self.helper(soFar + letter, rest[1:], result, mapping)
            
        
            