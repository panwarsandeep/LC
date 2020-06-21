
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

class Solution:
    ''' 
    Both recursive and non-recursive solution
    '''
    def checkSymm(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        print("left, right",left.val, right.val)
        if left.val == right.val:
            return self.checkSymm(left.right, right.left) and self.checkSymm(left.left, right.right)
        else:
            return False

    def isSymmetric(self, root):
        if root and (root.left and root.right) and root.left.val != root.right.val:
            return False
        elif not root:
            return False

        return self.checkSymm(root.left, root.right)
        
    def nonRecisSymmetric(self, root):
        if not root:
            return True
        queue = []
        queue.append([root,0])
        ind = 0
        sym = True
        
        while(queue):
            tl = []
            while queue and queue[0][1] == ind:
                te = queue.pop(0)
                if te[0] != None:
                    tl.append(te[0].val)
                    queue.append([te[0].left, ind+1])
                    queue.append([te[0].right,ind+1])
                else:
                    tl.append('$')
            if queue:    
                ind = queue[0][1]
            print(tl, tl[::-1])
            if tl != tl[::-1]:
                sym = False
                break
        return sym

            

def makeTree(vals):
    root = TreeNode(vals.pop(0))
    #tr = root
    queue = []
    queue.append(root)
    while vals:
        tr = queue.pop(0)
        try:
            tr.addLeft(TreeNode(vals.pop(0)))
            tr.addRight(TreeNode(vals.pop(0)))
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
        if i == ind:
            op += str(t.val) + "  "
        else:
            op += "\n"+" "*height+str(t.val) + "  "
            ind = i
        if t.getLeft():
            queue.append([t.getLeft(), i+1])
        if t.getRight():
            queue.append([t.getRight(), i+1])
        height //= 2
    print(op)

if __name__ == '__main__':
    
    import sys
    #sys.setrecursionlimit(10000)
    sol = Solution()
    val = [1,2,2,3,4,4,3]
    #val = [1,2,2,None,3,None,3]
    #val = [1,0]
    #val = []
    l = len(val)
    root = makeTree(val)
    printTree(root, l)
    r = sol.isSymmetric(root)
    print(r)
    r = sol.nonRecisSymmetric(root)
    print(r)
    