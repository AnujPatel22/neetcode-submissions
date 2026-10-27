# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth: int) -> None:
            if not node:
                return

            # If this is the first time reaching this depth,
            # this node MUST be the rightmost visible node.
            if depth == len(res):
                res.append(node.val)

            # Prioritize visiting the RIGHT branch first!
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
    