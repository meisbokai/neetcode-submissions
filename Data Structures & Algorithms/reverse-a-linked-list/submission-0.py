# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next # save the next node
            curr.next = prev # point current node to previous node
            prev = curr # set previous as current
            curr = next_node # set current as next node

        return prev

        