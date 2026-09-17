# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count total
        count = 0
        counter = head
        while counter != None:
            count += 1
            counter = counter.next

        print(count)

        # trivial case 1: Remove the only node
        if count == 1:
            return None

        point = head
        # case 2: removing the first node
        if count == n:
            head = point.next
            return head

        # case 3: removing last node
        if n == 1:
            while count != n+1:
                count -= 1
                # print(point.val)
                point = point.next
            point.next = None
            return head


        # case 4: removing node in the middle
        while count != n+1:
            count -= 1
            # print(point.val)
            point = point.next
        
        # skip
        # print(point.val)
        point.next = point.next.next
        # print(point.val)




        return head
        