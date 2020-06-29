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
    def getRightmost(self, node):
        prev = node
        while node:
            prev = node
            node = node.right
        return prev
    def flatten(self, root: TreeNode) -> None:
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            tl = self.getRightmost(root.left)
            tl.right = root.right
            root.right = root.left
            root.left = None
    

if __name__ == '__main__':
    
    import sys
    #sys.setrecursionlimit(10000)
    sol = Solution()
    
    val = [1, 2, 5, 3, 4, None, 6]
    l = len(val)
    root = makeTree(val)
    printTree(root, l)
    sol.flatten(root)
    tmp =  root
    print("result:")
    while tmp:
        print(" ", tmp.val)
        tmp = tmp.right