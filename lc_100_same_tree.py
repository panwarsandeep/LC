# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check_sim(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return (check_sim(p.left, q.left) and check_sim(p.right, q.right))
            return False
        return check_sim(p, q)