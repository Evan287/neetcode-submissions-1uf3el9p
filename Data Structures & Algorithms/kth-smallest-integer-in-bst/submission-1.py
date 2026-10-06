# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = float("inf")
        ans = 0
        def findMin(node):
            nonlocal k
            if not node or k <= 0:
                return 

            nonlocal res
            nonlocal ans
            findMin(node.left)
            k -= 1
            if k == 0:
                ans = node.val
            findMin(node.right)
        findMin(root)
        return ans
            

