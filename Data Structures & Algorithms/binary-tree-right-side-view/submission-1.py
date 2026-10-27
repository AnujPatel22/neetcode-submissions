# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return_vals = []

        def dfs(node, depth=0):
            if not node: return

            if len(return_vals) < ( depth + 1): return_vals.append(-1)

            return_vals[depth] = node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root)
        return return_vals
    