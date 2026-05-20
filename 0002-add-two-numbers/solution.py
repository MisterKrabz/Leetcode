# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        carry = 0
        head = ListNode()
        current = head
        
        while carry or l1 or l2: 
            val1 = 0
            val2 = 0
            if l1 is not None: 
                val1 = l1.val
            if l2 is not None: 
                val2 = l2.val
            add = val1 + val2 + carry
            if add > 9:
                carry = add // 10
                add = add % 10
            else: 
                carry = 0

            current.next = ListNode(add, None)
            current = current.next
            
            if l1: 
                l1 = l1.next 
            if l2: 
                l2 = l2.next
            
        return head.next
