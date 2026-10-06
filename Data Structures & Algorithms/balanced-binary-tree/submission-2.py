# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       #dfs function that returns height
          def dfs(root):
               if not root:
                    return [True, 0]
       #Recursively get results from each left and right children
               left, right = dfs(root.left), dfs(root.right)
       #A node is balanced if left and right are balanced and height diff no > 1
               balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
       #Height of the current node = 1 + max(leftheight, rightHeight)
               height = (1 + max(left[1], right[1]))
       #Run DFS on the root and return the isBalanced value
               return [balanced, 1+ max(left[1], right[1])]
          return dfs(root)[0]     