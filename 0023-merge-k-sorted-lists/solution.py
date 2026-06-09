# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        combined = list()
        for l in lists: 
            while l is not None: 
                combined.append(l.val)
                l = l.next
        combined.sort()

        if len(combined) == 0: 
            return None

        head = ListNode(combined.pop(0), None)
        current = head

        for num in combined: 
            current.next = ListNode(num, None)
            current = current.next 
        
        return head

        # i = 0
        # while i < len(lists): 
        #     if lists[i] is None: 
        #         lists.pop(i)
        #         continue
        #     i += 1


        # if not lists: 
        #     return None

        # head = None
        # index = 0
        # smallest = 99999
        # for i, node in enumerate(lists): 
        #     if node and node.val < smallest: 
        #         index = i
        #         smallest = node.val
        # head = lists[index]
        # current = head
        # if lists[index].next is not None: 
        #     lists[index] = lists[index].next
        # else: 
        #     lists.pop(index) 
        
        # while lists: 
        #     index = 0 
        #     smallest = lists[0].val 
        #     for i, node in enumerate(lists): 
        #         if node and node.val < smallest: 
        #             index = i 
        #             smallest = node.val 

        #     current.next = lists[index] 
        #     current = current.next 
        #     if lists[index].next is not None: 
        #         lists[index] = lists[index].next 
        #     else:
        #         lists.pop(index)
        # return head
