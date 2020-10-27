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
    def __init__(self):
        self.dp = {}
        self.dp[0] = []
        self.dp[1] = [TreeNode(0)]

    def allPossibleFBT(self, N):
        
        print("Rec call:", N)
        if N in self.dp:
            return self.dp[N]
        
        ans = []
        #print("Rec call:", N)
        for i in range(1, N, 2):
            left_tree = self.allPossibleFBT(i)
            right_tree = self.allPossibleFBT(N - i - 1)
            print("Rec stack:", N, len(left_tree), len(right_tree))
            for lt in left_tree:
                for rt in right_tree:
                    tnode = TreeNode(0)
                    tnode.left = lt
                    tnode.right = rt
                    ans.append(tnode)
        self.dp[N] = ans
        return self.dp[N]

                

def get_flat_tree(root, ftree):
    if not root:
        ftree.append(None)
        return
    ftree.append(root.val)
    get_flat_tree(root.left, ftree)
    get_flat_tree(root.right, ftree)

    
if __name__ == '__main__':
    sol = Solution()

    n = 7
    print(n)
    r = sol.allPossibleFBT(n)
    print(r)
    '''
    t = []
    for v in r:
        tl = []
        get_flat_tree(v, tl)
        print(tl)
    '''

    