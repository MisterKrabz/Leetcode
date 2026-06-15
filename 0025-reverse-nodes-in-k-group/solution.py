# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        while head is not None: 
            nodes.append(head)
            head = head.next 
        
        head = nodes[k - 1]
        prev = ListNode()

        while len(nodes) >= k: 
            i = k - 1
            while i >= 0: 
                prev.next = nodes.pop(i)
                prev = prev.next 
                i -= 1

        for node in nodes: 
            prev.next = node
            prev = prev.next 
        
        prev.next = None
        return head
