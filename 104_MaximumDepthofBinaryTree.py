# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 76 ms [23%]

        if root is None: #!
            return 0

        return self.helper(root, 1)

    def helper(self, node, curDepth):
        #if node.left is None and node.right is None: # Line 18: AttributeError: 'NoneType' object has no attribute 'left'
        if node is None:
            return curDepth

        leftDepth = rightDepth = curDepth
        #leftDepth, rightDepth = curDepth # Line 22: TypeError: 'int' object is not iterable
        if node.left is not None:
            leftDepth =  self.helper(node.left, curDepth+1)

        if node.right is not None:
            rightDepth = self.helper(node.right, curDepth+1)

        return max(leftDepth, rightDepth)
