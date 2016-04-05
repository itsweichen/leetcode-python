# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # 04/05/2016
        # O(n) - 60 ms [4.3%]

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while(current.next is not None and current.next.next is not None):
            first = current.next
            second = first.next
            first.next = second.next
            second.next = first
            current.next = second
            current = first
            
        return dummy.next