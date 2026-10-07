# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        queue = deque()
        def bfs(root):
            if root:
                queue.append(root)
            level = 0
            while len(queue) > 0:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    res[level].append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level += 1
        bfs(root)
        return [val for val in res.values()]
        

