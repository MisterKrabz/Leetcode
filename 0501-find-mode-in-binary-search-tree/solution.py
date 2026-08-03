# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        items = dict()
        while stack: 
            node = stack.pop(-1)

            if node.right: 
                stack.append(node.right)
            if node.left: 
                stack.append(node.left)
            
            if node.val in items:
                items[node.val] += 1
            else: 
                items[node.val] = 1
        
        ret = []
        m = 0
        for key, val in items.items(): 
            if val > m: 
                ret = [key]
                m = val
            elif val == m: 
                ret.append(key)

        return ret


