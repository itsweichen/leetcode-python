# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        # 06/26/2016
        

        n = len(points)

        if n <= 1: return n

        maxNum = 1
        for i in range(n):
            x1, y1 = points[i].x, points[i].y
            slp = {}

            for j in range(i+1, n):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2:
                    if y1 == y2:
                        k = "o"
                    else:
                        k = "v"
                else:
                    k = (y1-y2) / (float(x1)-x2)
                if k in slp:
                    slp[k] += 1
                else:
                    slp[k] = 1

            overlap = slp.pop("o") if "o" in slp else 0

            if len(slp) == 0:
                maxNum = max(overlap+1, maxNum)
            else:
                maxNum = max(slp[max(slp, key=slp.get)]+overlap+1, maxNum)

        return maxNum
