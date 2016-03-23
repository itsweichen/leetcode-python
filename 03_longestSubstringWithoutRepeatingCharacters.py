# 03/22/2016

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # [6.5%]
        
        # Understand the question! 1) substring(contiguous) 2) without repeating char

        # check for empty string!
        if len(s) == 0 or s is None:
            return 0
        
        max = 1
        letterSet = {}
        letterSet[s[0]] = 0
        L = [1]
        for i in range(1, len(s)):
            if s[i] in letterSet:
                sameCharIndex = letterSet[s[i]]
                curValue = i - sameCharIndex
                L.append(curValue)
                if curValue > max:
                    max = curValue
                letterSet = {}
                for j in range(sameCharIndex+1, i+1):
                    letterSet[s[j]] = j
            else:
                letterSet[s[i]] = i
                L.append(L[i-1]+1)
                if L[i-1]+1 > max:
                    max = L[i-1] + 1
            
        return max
                
        
            