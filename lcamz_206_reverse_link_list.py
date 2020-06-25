
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, val):
        tn = ListNode(val)
        self.next = tn
        
class Solution:
    def reverseList(self, head):
        if not head:
            return None
        p = None
        q = head
        r = head.next
        while q.next:
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p
        head = q
        return head
    def recReverseList(self, prev, node, rhead):
        if node == None:
            rhead.append(None)
            return node
        if node.next == None:
            rhead.append(node)
            node.next = prev
            return
        self.recReverseList(node, node.next, rhead)
        node.next = prev
            


def printList(node):
    while node:
        print(node.val,"  ",end='')
        node = node.next
    print("")

if __name__ == '__main__':
    sol = Solution()
    
    nums = [7,1,5,3,6,4]
    head = None
    tnode = None
    for n in nums:
        newNode = ListNode(n)
        if head == None:
            head = newNode
            tnode = head
            continue
        tnode.next = newNode
        tnode = newNode

    printList(head)
    nlist = []
    #nlist = sol.reverseList(head)
    sol.recReverseList(None, head, nlist)
    print("new list: ")
    printList(nlist[0])
    #r = sol.maxProfit(nums)
    #print(r)