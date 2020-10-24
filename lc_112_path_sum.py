# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, tsum: int) -> bool:
        def calc_sum(root, rsum, tsum):
            if root == None:
                return False

            rsum += root.val
            if not root.left and not root.right and rsum == tsum:
                return True

            if calc_sum(root.left, rsum, tsum) or calc_sum(root.right, rsum, tsum):
                return True

            return False

        rsum = 0
        return calc_sum(root, rsum, tsum)