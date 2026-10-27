# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
      # Map each value to its index in inorder for O(1) lookup
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        
        # Track our position in preorder
        preorder_idx = 0

        def array_to_tree(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            
            # Base case: no elements to construct the subtree
            if in_left > in_right:
                return None

            # 1. The current preorder element is the root of this subtree
            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)
            preorder_idx += 1

            # 2. Get root's position in inorder to split left and right subtrees
            mid = inorder_idx_map[root_val]

            # 3. Build left subtree first (matches preorder order: root -> left -> right)
            root.left = array_to_tree(in_left, mid - 1)
            # 4. Build right subtree
            root.right = array_to_tree(mid + 1, in_right)

            return root

        return array_to_tree(0, len(inorder) - 1)