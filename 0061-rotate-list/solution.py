# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: 
            return None
        
        current = head
        length = 1
        while current.next is not None: 
            current = current.next 
            length += 1

        if length == 1: 
            return head
        
        current.next = head 

        k = k % length 
        steps = length - k
        
        for i in range(steps): 
            current = current.next 
        
        head = current.next
        current.next = None

        return head
        

