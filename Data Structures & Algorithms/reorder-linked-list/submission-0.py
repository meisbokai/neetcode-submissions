# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        prev = None
        curr = head
        count = 0

        while curr:
            new_node = ListNode(curr.val)
            new_node.next = prev

            prev = new_node
            curr = curr.next
            count += 1

        return prev, count

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Original list
        forw = head

        # Separate reversed copy
        rev, count = self.reverseList(head)

        # Build the reordered list
        result = ListNode(0)
        curr = result

        for i in range(count):
            if i % 2 == 0:
                curr.next = forw
                forw = forw.next
            else:
                curr.next = rev
                rev = rev.next

            curr = curr.next

        # Terminate the list
        curr.next = None
                

        