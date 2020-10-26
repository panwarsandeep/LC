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
    def zigzagLevelOrder(self, root):
        def list_append(lst, tnode, order):
            if order == 1:
                lst.insert(0, tnode.val)
            else:
                lst.append(tnode.val)
        if not root:
            return []
        Q = [root]
        Q.append(None)
        lvl_ord = 0
        global_list = []
        while  len(Q) > 1:
            lvl_list = []
            while Q[0] != None:
                tval = Q.pop(0)
                list_append(lvl_list, tval, lvl_ord)
                if tval.left:
                    Q.append(tval.left)
                if tval.right:
                    Q.append(tval.right)
            Q.pop(0)
            global_list.append(lvl_list)
            Q.append(None)
            lvl_ord ^= 1
        return global_list
                



if __name__ == '__main__':
    sol = Solution()

    val = [1, 2, 5, 3, 4, None, 6]
    l = len(val)
    root = makeTree(val)
    printTree(root, l)
    r = sol.zigzagLevelOrder(root)
    print(r)