class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        # 04/20/2016
        # O(3n) - 76 ms [10%]

        # assume that input is correct
        # 1) 加到一个list 2) iterate list来看结果 3)再iterate一遍组成string

        dirs = []
        length = len(path)

        dirName = ""

        # 1)
        for char in path:
            if char != "/":
                dirName += char
            else:
                if dirName != "":
                    dirs.append(dirName)
                    dirName = ""
        # last name
        if dirName != "":
            dirs.append(dirName)
            dirName = ""

        # 2)
        res = []

        for dirName in dirs:
            if dirName == ".":
                continue
            if dirName == "..":
                if len(res) != 0:
                    res.pop()
                continue
            res.append(dirName)

        # 3)
        result = ""
        for dirName in res:
            result += "/" + dirName


        return result if len(result) > 0 else "/"
