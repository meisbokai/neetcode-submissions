# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # O(N x K)
        nodes_arr = []
        for l in lists:
            nodes = []
            while l != None:
                nodes.append(l.val)
                l=l.next
            nodes_arr.append(nodes)
            # print(nodes)

        # print(nodes_arr)
        # print(*nodes_arr)


        # heapq merge: (O(N log K)), 
        combined_iterator = heapq.merge(*nodes_arr)

        # O (N)
        answer = ListNode()
        pointer = answer
        for i in combined_iterator:
            # print(i)
            pointer.next = ListNode(i)
            pointer = pointer.next

        return answer.next