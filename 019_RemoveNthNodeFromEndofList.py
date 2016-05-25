# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # 5/25/2016
        # 48ms [60%]
        
        # One pass
        # construct a linked-list of size n+1, move this list each time
        
        _head = ListNode(head)
        _cur = _head
        cur = head
        
        for i in xrange(n):
            _cur.next = ListNode(cur.next)
            _cur = _cur.next
            cur = cur.next
        
        if cur is None:
            return head.next
                
        while cur.next != None:
            _head = _head.next
            _cur.next = ListNode(cur.next)
            _cur = _cur.next
            cur = cur.next
        
        _head.val.next = _head.val.next.next
        return head
                