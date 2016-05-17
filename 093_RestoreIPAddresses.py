class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        # 5/17/2016
        # 60 ms [38%]
        
        valid = {}
        for i in xrange(256):
            valid[str(i)] = '0'

        res = []

        self.solve([], s, valid, res)

        return res # remember to return!!!


    def solve(self, soFar, rest, valid, res):
        if len(soFar) == 3:
            if rest in valid:
                soFar.append(rest)
                ip = '.'.join(soFar)
                res.append(ip)
                return
            else:
                return

        if rest == "":
            return

        for i in xrange(1, len(rest)+1):
            if i == 4:
                return
            option = rest[:i]
            if option in valid:
                self.solve(soFar+[rest[:i]], rest[i:], valid, res)
