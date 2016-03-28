# 11. Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # O(n), 88 ms [35%]
        l, r = 0, len(height) - 1
        
        if r <= 0:
            return 0
        
        maxArea = r * min(height[l], height[r])
        
        while (r - l > 1):
            if height[l+1] > height[l]:
                l = l + 1
                maxArea = max(maxArea, (r - l)*min(height[l], height[r]))
            elif height[r-1] > height[r]:
                r = r - 1
                maxArea = max(maxArea, (r - l)*min(height[l], height[r]))
            else:
                if height[l] > height[r]:
                    r = r - 1
                else:
                    l = l + 1

        return maxArea

        # 还有更简单的，只需要要移动那个矮个子的就好了。