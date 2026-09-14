# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode()
        head = answer

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    answer.next = list1
                    list1 = list1.next
                else:
                    answer.next = list2
                    list2=list2.next
            elif list1:
                answer.next = list1
                list1 = list1.next
            elif list2:
                answer.next = list2
                list2 = list2.next
            answer = answer.next

        return head.next
        