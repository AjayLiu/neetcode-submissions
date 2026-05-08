"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        randomDict = {}
        ptrDict = {}
        oldPtr = head
        newPrev = Node(head.val, None, None)
        randomDict[newPrev] = head.random
        ptrDict[head] = newPrev
        newHead = newPrev
        oldPtr = oldPtr.next
        while oldPtr:
            newNode = Node(oldPtr.val, None, None)
            randomDict[newNode] = oldPtr.random
            ptrDict[oldPtr] = newNode
            newPrev.next = newNode
            newPrev = newNode
            oldPtr = oldPtr.next
        
        toReturn = newHead
        while newHead:
            r = randomDict[newHead]
            if r:
                newHead.random = ptrDict[r]
            newHead = newHead.next
        
        return toReturn