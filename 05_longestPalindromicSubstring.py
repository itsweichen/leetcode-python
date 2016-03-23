# 03/22/2016

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # DP - O(n^2)
        # Time Limit Exceeded! = =
        
        n = len(s)
        
        if(n==1):
            return s
        
        M = [[0 for x in range(n)] for x in range(n)]
        P = [[0 for x in range(n)] for x in range(n)] # pointer to track which char
        # "ld", "l", "d"
        
        for i in range(n):
            M[i][i] = 0
        
        for x in range(1, n):
            for i in range(0, n-x):
                j = i + x
                if(s[i] == s[j]):
                    M[i][j] = M[i+1][j-1] + 2
                    P[i][j] = "ld"
                else:
                    if (M[i][j-1] > M[i+1][j]):
                        M[i][j] = M[i][j-1]
                        P[i][j] = "l"
                    else:
                        M[i][j] = M[i+1][j]
                        P[i][j] = "d"
        
        i = 0
        j = n - 1
        while(i != j):
            if(P[i][j] == "ld"):
                return s[i:j+1]
            elif(P[i][j] == "l"):
                j = j - 1
            else:
                i = i + 1
        return s[i]

