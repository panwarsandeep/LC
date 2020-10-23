# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        if not root:
            return []
        queue.append(root)
        queue.append(None)
        res = []
        while len(queue) > 1:
            tmp_res = []
            while queue[0] != None:
                p_node = queue.pop(0)
                tmp_res.append(p_node.val)
                if p_node.left:
                    queue.append(p_node.left)
                if p_node.right:
                    queue.append(p_node.right)
            queue.pop(0)
            queue.append(None)
            res.append(tmp_res)
        return reversed(res)