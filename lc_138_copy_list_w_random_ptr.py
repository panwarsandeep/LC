
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        itr = head
        newhead = None
        map = defaultdict(Node)
        while itr:
            tmp = Node(itr.val, None, None)
            if newhead == None:
                newhead = tmp
                new = tmp
            else:
                new.next = tmp
                new = tmp
            if itr.random == None:
                new.random = None
            map[itr] = tmp
            itr = itr.next
        
        itr = head
        new = newhead
        while itr:
            if itr.random != None:
                new.random = map[itr.random]
            new = new.next
            itr = itr.next
        return newhead