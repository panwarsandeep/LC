# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    '''
    for each node get the max sum for left and right node and keep updated the global maximum
    example:
           -10
        9       20
            15      7
    
    above tree is: [-10,9,20,null,null,15,7]
    using the dfs approaach, when doing calculation for node 20
    the control reaches the left most i.e. node 15 (value 15). this node has no further left or right child
    hence the left, right for this node will be 0 and local max would be max( max(0, 0)+15, 15) = 15
    similarly max right (for parent node 20) would be 7.
    now if the tree rooted at 20 has the max path then it would include the sum of left, right and root which would be: 15 + 20 + 7 = 42, in this case
    the path is 15 -> 20 -> 7 (each path is traced exactly once)
    if not, then we need to move up, but in that case we can not take both 15, and 7 because that will not be a valid path according to the problem statement
    the reason is the path should not be retraced e.g. path involving -10 could be: -10 -> 20 -> 15 or -10 -> 20 -> 7. we can't include both 15 and 7
    in single path including node -10. For this reason, if we want to move to parent of any node, take the max of its left and right and include that.

    '''
    def maxPathSum(self, root):
        self.result = -sys.maxsize
        def get_max_sum(root):
            if not root:
                return 0
            left = get_max_sum(root.left,)
            right = get_max_sum(root.right)
            lmx = max(max(left, right)+root.val, root.val)
            gmx = max(lmx, left + right + root.val)
            self.result =  max(self.result, gmx)
            return lmx
        get_max_sum(root)
        return self.result