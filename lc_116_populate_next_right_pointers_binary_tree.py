import sys
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None
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
    root = Node(vals.pop(0))
    #tr = root
    queue = []
    queue.append(root)
    while vals:
        tr = queue.pop(0)
        try:
            tv = vals.pop(0)
            if tv:
                tr.addLeft(Node(tv))
            tv = vals.pop(0)
            if tv:
                tr.addRight(Node(tv))
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

def printTreeNext(root):
    import math
    queue = []
    queue.append([root,0])
    res = []
    while(queue):
        t,i = queue.pop(0)
        tn = '#' if t.next == None else t.next.val
        res.append((t.val, tn))
        if t.getLeft():
            queue.append([t.getLeft(), i+1])
        if t.getRight():
            queue.append([t.getRight(), i+1])
    return res

class Solution:
    '''
    The idea here is to connect left and right subtree.
    each tree's parent's next node has already been set to its peer (right sub tree) hence
    take advantage of that property
    '''
    def connect(self, root):
        def fillNext(root):
            if not root or \
                (not root.left and not root.right):
                return
            root.left.next = root.right
            root.right.next = root.next.left if root.next else None
            fillNext(root.left)
            fillNext(root.right)
        fillNext(root)
        return root
    

if __name__ == '__main__':
    
    import sys
    sol = Solution()
   
    tree = [1,2,3,4,5,6,7]
    tree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    root = makeTree(tree)
    rt = printTreeNext(root)
    print(rt)
    sol.connect(root)
    rt = printTreeNext(root)
    print(rt)
    #r = sol.isValidBST(root)
    #print(r)