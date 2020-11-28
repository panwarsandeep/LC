# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def solve(root, from_left=False):
            nonlocal sum
            if not root:
                return
            solve(root.left, True)
            if from_left and not root.right and not root.left:
                sum += root.val
            else:
                solve(root.right)
        sum = 0
        solve(root)
        return sum