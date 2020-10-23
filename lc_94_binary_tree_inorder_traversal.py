# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def in_o_traverse(root, res):
            if not root:
                return root
            in_o_traverse(root.left, res)
            res.append(root.val)
            in_o_traverse(root.right, res)
        
        res = []
        in_o_traverse(root, res)
        return res