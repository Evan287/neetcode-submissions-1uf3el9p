# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Level Order Traversal, BFS
        if not root: 
            return []
        q = deque([(root, 0)]) #(node, col)
        min_col, max_col = 0, 0
        cols = defaultdict(list) #map col index to list of value

        while q:
            node, col = q.popleft()
            cols[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            #if right then we increment col, else decrement
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        return [cols[c] for c in range(min_col, max_col + 1)]
            
