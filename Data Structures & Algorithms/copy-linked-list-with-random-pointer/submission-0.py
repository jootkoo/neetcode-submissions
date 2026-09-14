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
        oldToCopy = {None : None} #hashmap, initialize None for curr.next edgecase
        curr = head #current pointer

        while curr: #while not empty, first iteration, create copies put in hashmap
            copy = Node(curr.val) #initialize a NEW copy using the Node constructor
            #if not use constructor it will just point to the orignial list 
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head #restart at the beginning
        while curr:
            copy = oldToCopy[curr] #grab the copy of the current node
            #set the pointer
            copy.next = oldToCopy[curr.next] #have this copy point to the next node
            copy.random = oldToCopy[curr.random] #have this copy point to the random node
            curr = curr.next
        return oldToCopy[head]
