# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        nodes = []

        while current is not None: 
            nodes.append(current)
            current = current.next
            print(current)
        
        if len(nodes) == 1: 
            return None
        if n == 1:
            nodes[len(nodes) - 2].next = None
        elif n == len(nodes): 
            head = nodes[1]           
        else:
            nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n + 1]
        
        return head
