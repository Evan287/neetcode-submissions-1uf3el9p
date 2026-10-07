# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Two helper operations

        #Compare trees
        def compareTrees(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return compareTrees(p.left, q.left) and compareTrees(p.right, q.right)
            else:
                return False

        #Find subRoot node in root
        if not root:
            return False
        curr = root
        if compareTrees(curr, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        else:
            return False

    

