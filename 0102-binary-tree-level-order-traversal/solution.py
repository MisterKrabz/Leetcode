# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        queue = deque()
        queue.append(root)
        current_level = [root]

        ret = []

        while current_level: 
            next_level = []

            part = []
            for node in current_level: 
                part.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            ret.append(part)

            current_level = next_level

        return ret 

