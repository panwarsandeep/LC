# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        t_l1 = l1
        t_l2 = l2
        carry = 0
        head = None
        tmp = None
        while t_l1 and t_l2:
            num = t_l1.val + t_l2.val + carry
            carry = num // 10
            num %= 10
            if head == None:
                head = ListNode(num)
                tmp = head
            else:
                tmp.next = ListNode(num)
                tmp = tmp.next
            t_l1 = t_l1.next
            t_l2 = t_l2.next

        rem_lst = t_l1 if t_l1 else t_l2
        while rem_lst:
            num = rem_lst.val + carry
            carry = num // 10
            num %= 10
            tmp.next = ListNode(num)
            tmp = tmp.next
            rem_lst = rem_lst.next
        if carry:
            tmp.next = ListNode(carry)
        return head


def printList(node):
    while node:
        print(node.val, " ", end='')
        node = node.next
    print("")

def build_link_list(arr):
    head = None
    tmp = None
    for val in arr:
        if head == None:
            head = ListNode(val)
            tmp = head
        else:
            tmp.next = ListNode(val)
            tmp = tmp.next
    return head

if __name__ == '__main__':
    sol = Solution()
    
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    ll1 = build_link_list(l1)
    ll2 = build_link_list(l2)
    r = sol.addTwoNumbers(ll1, ll2)
    printList(r)
    

