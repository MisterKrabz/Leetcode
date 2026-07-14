# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head 
        nodes = []
        while current is not None: 
            nodes.append(current)
            current = current.next 

        newNodes = []
        i = 0
        while i < len(nodes) // 2: 
            newNodes.append(nodes[i])
            newNodes.append(nodes[len(nodes) - i - 1])
            i += 1
        if len(nodes) % 2 == 1: 
            newNodes.append(nodes[(len(nodes) - 1)//2])

        head = newNodes[0]
        current = head
        i = 1
        while i < len(newNodes): 
            current.next = newNodes[i]
            current = current.next
            i += 1
        current.next = None

        return head

        
