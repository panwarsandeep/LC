# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        cur_path = []

        def get_paths(root, cur_path):
            cur_path.append(str(root.val))
            if root.left == None and root.right == None:
                paths.append('->'.join(cur_path))
                return

            if root.left:
                get_paths(root.left, cur_path)
                cur_path.pop()
            if root.right:
                get_paths(root.right, cur_path)
                cur_path.pop()
        
        if not root:
            return root
        get_paths(root, cur_path)
        return paths
        