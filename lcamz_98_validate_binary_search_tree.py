import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def addLeft(self, chld):
        if self.left == None:
            self.left = chld
    def addRight(self, chld):
        if self.right == None:
            self.right = chld
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

def makeTree(vals):
    root = TreeNode(vals.pop(0))
    #tr = root
    queue = []
    queue.append(root)
    while vals:
        tr = queue.pop(0)
        try:
            tv = vals.pop(0)
            if tv:
                tr.addLeft(TreeNode(tv))
            tv = vals.pop(0)
            if tv:
                tr.addRight(TreeNode(tv))
        except:
            pass
        if tr.getLeft():
            queue.append(tr.getLeft())
        if tr.getRight():
            queue.append(tr.getRight())

    return root

def printTree(root, l):
    import math
    queue = []
    queue.append([root,0])
    ind = 0
    op = ""
    height = math.floor(math.log2(l))
    psp = " "*height
    op = psp
    while(queue):
        t,i = queue.pop(0)
        v = t.val if t.val is not None else '-'
        if i == ind:
            op += str(v) + "  "
        else:
            op += "\n"+" "*height+str(v) + "  "
            ind = i
        if t.getLeft():
            queue.append([t.getLeft(), i+1])
        if t.getRight():
            queue.append([t.getRight(), i+1])
        height //= 2
    print(op)
class Solution:
    def checkMaxMin(self, root, val, is_max):
        if not root:
            return True
        elif (root.val >= val and is_max) or \
            (root.val <= val and not is_max):
            return False
        else:
            return self.checkMaxMin(root.left, val, is_max) and \
                self.checkMaxMin(root.right, val, is_max)

    def inOrder(self, root, v):
        if root == None:
            return
        self.inOrder(root.left, v)
        v.append(root.val)
        self.inOrder(root.right, v)
    
    def isValidBST(self, root):
        v = []
        self.inOrder(root, v)
        for j in range(1, len(v)):
            if v[j] <= v[j-1]:
                return False
        return True
    '''
    def isValidBST(self, root):
        if root == None:
            return True
        elif self.checkMaxMin(root.left, root.val, True) and \
            self.checkMaxMin(root.right, root.val, False):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False
    '''
    

if __name__ == '__main__':
    
    import sys
    #sys.setrecursionlimit(10000)
    sol = Solution()
    val = [5, 1, 4, None, None, 3, 6]
    val = [2, 1, 3]
    val = [10,5,15,None,None,6,20]
    #val = [1,2,2,None,3,None,3]
    #val = [1,0]
    #val = []
    l = len(val)
    root = makeTree(val)
    printTree(root, l)
    r = sol.isValidBST(root)
    print(r)