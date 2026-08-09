# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        stack = []
        node = root

        while node:
            stack.append(node)
            node = node.left

        while stack:
            node = stack.pop()
            ret.append(node.val)

            node = node.right

            while node:
                stack.append(node)
                node = node.left

        return ret


