# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #1 use hash map
        # 92 ms [35%]
        """
        cur = head
        visited = {}
        while cur is not None:
            if cur in visited:
                return True
            else:
                visited[cur] = 0
            cur = cur.next
        return False
        """

        #2 w/o extra space

        # Can I do this? lol
        # 88 ms [50%]
        """
        if head is None:
            return False

        cur = head.next

        while cur is not None:
            if cur is head:
                return True
            prev = cur
            cur = cur.next
            prev.next = head
        return False
        """

        #3 racing
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True
