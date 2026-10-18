# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = dict()

        q = [root]
        while q: 
            current = q.pop(-1) 
            if current.left: 
                q.append(current.left)
                parent[current.left] = current 
            if current.right: 
                q.append(current.right)
                parent[current.right] = current 
        
        ret = []
        visited = {target}
        q = [(target, 0)]
        while q: 
            if q[-1][1] == k:
                current = q.pop(-1)[0]
                ret.append(current.val)
                continue
            index = q[-1][1]
            current = q.pop(-1)[0]
            if current.left and current.left not in visited: 
                q.append((current.left, index + 1))
                visited.add(current.left)
            if current.right and current.right not in visited: 
                q.append((current.right, index + 1))
                visited.add(current.right)
            if current in parent and parent[current] not in visited: 
                q.append((parent[current], index + 1))
                visited.add(parent[current])

        return ret 

        

