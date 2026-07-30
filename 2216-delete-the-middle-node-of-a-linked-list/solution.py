# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head: 
            return None 
        if not head.next: 
            return None
        
        p1 = head 
        p2 = head.next 

        if p2.next is None: 
            p1.next = None 
            return p1 

        while p2 is not None: 
            if p2.next and p2.next.next: 
                p2 = p2.next 
                p2 = p2.next 
                p1 = p1.next
            else: 
                break 

        p1.next = p1.next.next
        return head 

