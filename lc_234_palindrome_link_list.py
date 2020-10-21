
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, val):
        tn = ListNode(val)
        self.next = tn
        
class Solution:
    def isPalindrome(self, head):
        def rev_list(node):
            prev = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
        if not head or not head.next:
            return  True
        # find the middle node
        s_ptr = head
        f_ptr = head.next
        while f_ptr and f_ptr.next:
            f_ptr = f_ptr.next.next
            s_ptr = s_ptr.next
        
        # reverse from middle node onwards
        # this will take care of both cases i.e. even/odd number of elements because
        # we are starting loop with reversed list (which will be smaller in case of odd number of elements)
        # and after comparision the middle element will anyway be left out
        r_list = rev_list(s_ptr.next)
        rev = r_list
        fwd = head
        while rev:
            if rev.val != fwd.val:
                return False
            rev = rev.next
            fwd = fwd.next
        return True

        '''
        recursive sol with additional space

        def solve_palindrome(node, stack):
            if node == None:
                return True
            stack.append(node.val)
            if not solve_palindrome(node.next, stack):
                return False
            
            if node.val == stack[0]:
                stack.pop(0)
                #print(stack)
                ret =  True
            else:
                ret = False
            return ret
        stack = []
        return solve_palindrome(head, stack)
        '''
            


def reverseList(head):
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
def recReverseList(node):
    if node == None or node.next == None:
        return node
    new_head = recReverseList(node.next)
    node.next.next = node
    node.next = None
    return new_head
    
            


def printList(node):
    while node:
        print(node.val,"  ",end='')
        node = node.next
    print("")

def build_list(nums):
    head = None
    for n in nums:
        new_node = ListNode(n)
        if head == None:
            head = new_node
            tnode = head
            continue
        tnode.next = new_node
        tnode = new_node
    return head

if __name__ == '__main__':
    sol = Solution()
    
    nums = [1, 2, 2, 1]
    nums = [1, 0, 1]
    head = build_list(nums)

    printList(head)
    r = sol.isPalindrome(head)
    print(r)

    lst = [1,2,3,4,5,6,7]
    lst = build_list(lst)
    printList(lst)
    new_lst = recReverseList(lst)
    printList(new_lst)