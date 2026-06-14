# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: 
            return head

        prev = None
        p1 = head
        p2 = head.next 

        while p1 and p2: 
            p1.next = p2.next
            p2.next = p1

            if prev: 
                prev.next = p2
                prev = p1
            else: 
                prev = p1
                head = p2
            if p2.next is not None and p1.next is not None: 
                temp = p1.next.next
                p1 = p2.next.next
                p2 = temp
            else: 
                break
        
        return head
            
            
            
                






