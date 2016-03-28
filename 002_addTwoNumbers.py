# 03/21/2016

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # O(n) [8%]
        carry = 0
        dummy = ListNode(0)
        current = dummy
        
        while l1 or l2: # the way to check if it's none, or `while l1 is not None`
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val / 10
            val = val % 10
            current.next = ListNode(val) # store the value in *next* node
            current = current.next
        
        if carry == 1:
            current.next = ListNode(carry)
            
        return dummy.next
            