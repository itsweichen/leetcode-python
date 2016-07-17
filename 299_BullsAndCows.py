class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        # 07/17/2016
        # 68 ms [82%]

        bull, cow = 0, 0
        secret_dict = {}
        bull_loc = set()

        for i in range(len(secret)):
            sec_cur = secret[i]
            if sec_cur == guess[i]:
                bull += 1
                bull_loc.add(i)
            else:
                if sec_cur in secret_dict:
                    secret_dict[sec_cur] += 1
                else:
                    secret_dict[sec_cur] = 1

        for i in range(len(guess)):
            gue_cur = guess[i]
            if gue_cur in secret_dict and secret_dict[gue_cur] > 0 and i not in bull_loc:
                secret_dict[gue_cur] -= 1
                cow += 1

        return str(bull) + "A" + str(cow) + "B"
