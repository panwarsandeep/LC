# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getHeight(self, root):
        if not root:
            return 0
        
        lh = self.getHeight(root.left) 
        rh = self.getHeight(root.right) 
        #print(root.val, lh, rh)
        if lh + rh > self.dm:
            self.dm = lh + rh 
            #print(self.dm)
        return max(lh, rh)+1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dm = 0
        h = self.getHeight(root)
        return self.dm
'''
if __name__ == '__main__':
    sol = Solution()

'''