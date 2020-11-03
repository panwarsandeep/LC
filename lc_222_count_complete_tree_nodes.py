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
    '''
    The idea is to take advantage of property i.e. complete binary tree.
    if the last level is complete then the number of nodes will be 2^h -1 (h is height of binary tree)
    for each node, we can have expected number of nodes its left and right sub tree must have (if it is a complete binary tree filled till last level)
    e.g. lets consider the example:
         1
        / \
       2    3
      / 
     4   
     if it was a tree like following:
         1
        / \
       2    3
      / \  / \
     4   5 6  7
    Number of nodes would be 2^3 - 1 = 7 (here height is 3)
    but thats not the case in our example.
    Also another important thing to note is "all nodes in the last level are as far left as possible"
    so if any left subtree doesn't have expected number of nodes, we don't need to calculate its right subtree manually, instead we can
    apply math and get the number of nodes directly, as follows:
    (expected_no_of_subtree - 1) / 2    =>  good to take some examples to understand this logic

    In the first tree above, the expected no. of nodes at node '1' would be = 7 (considering it is comoplete till last level)
    reducing 1 (for the root node itself), 7 - 1 = 6 and evenly dividing it to left and right child i.e. 6/2 = 3.
    means the left and right subtree of node '1' can have max 3 nodes (if they are full binary tree) but somehow if its left subtree doesn't have
    desired number of nodes means the left sub-tree itself is not coomplete till last level so there is no way its right subtree will have any elements
    at the last level. keeping this in mind ("all nodes in the last level are as far left as possible"), calculation for the nodes in right sub-tree would be:
    (expected number of nodes - 1) / 2
    lets see an example:
    - at node '1', expected nodes are 7
    - - 7 - 1 = 6 / 2  = 3
    - - check left node '2' with expected nodes as '3'
    - - 3 - 1 = 2 / 2 = 1, expected no of nodes for its (node '2') left, right sub-tree is 1
    - - node '2' has no. of left node as 1 (node '4' only) so calculate right node as well which is not present
    - - total number of nodes till node '2' (including itself) is 2 (2 -> 4) but expected here is 3.
    - - since left sub-tree of '1' (which is '2') has less number of nodes than expected, no need to calculate right sub-tree:
    - - instead nodes in its right subtree will be (3-1)/2 = 1.
    - - just add that value with left value and also add 1 for the current node and return

    This logic avoid traversing right subtree when not necessary.
    '''
    def countNodes(self, root):
        def count_helper(root, exptd):
            if not root:
                return 0
            left = count_helper(root.left, (exptd - 1)//2)
            if left < ((exptd - 1) // 2):
                return left + (exptd - 1) // 4 + 1
            right = count_helper(root.right, (exptd - 1)//2)
            return left + right + 1
        # get the height of the tree
        if not root:
            return 0
        height = 0
        tnode = root
        while tnode:
            height += 1
            tnode = tnode.left
        max_possible_nodes = (2 ** height) - 1
        return count_helper(root, max_possible_nodes)
                



if __name__ == '__main__':
    sol = Solution()

    val = [1, 2, 3, 4, 5, 6]
    l = len(val)
    root = makeTree(val)
    printTree(root, l)
    r = sol.countNodes(root)
    print(r)