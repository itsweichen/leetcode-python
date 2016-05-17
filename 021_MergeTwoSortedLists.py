# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 5/16/2016
        # 56 ms [50%]

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        cur = head

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next #!!!

        while l1 != None:
            cur.next = l1
            l1 = l1.next
            cur = cur.next #!!!

        while l2 != None:
            cur.next = l2
            l2 = l2.next
            cur = cur.next #!!!

        return head
