# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # 5/27/2016
        # 56 ms [54%]

        #PART1: find the length of the list
        n = 0 # length of the list
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next

        if n == 0:
            return head

        k = k % n # n cannot be zero
        if k == 0:
            return head

        #PART2: calculate the newHeadIndex
        newHeadIndex = n + 1 - k # 2...n

        #PART3: reconstruct the list
        cur = head
        i = 1
        while cur is not None:
            prev = cur
            cur = cur.next # should be visited before change
            if i == newHeadIndex - 1:
                prev.next = None
            if i == newHeadIndex:
                newHead = prev
            i += 1
        prev.next = head

        return newHead
