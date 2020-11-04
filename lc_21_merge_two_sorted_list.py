# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newlist = None
        newhead = None
        while l1 and l2:
            tmp = None
            if l1.val <= l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            tmp.next = None
            if newlist == None:
                newlist = tmp
                newhead = newlist
                continue
            newlist.next = tmp
            newlist = newlist.next
        tmp = l1 or l2
        if not newhead:
            newhead = tmp
        else:
            while tmp:
                newlist.next = tmp
                tmp = tmp.next
                newlist = newlist.next
            newlist.next = None
        return newhead