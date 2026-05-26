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

        oldToCopy = {None: None}

        #one pass to store copy of nodes into hashmap
        curr = head

        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        #two pass to create links
        curr = head

        while curr:
            #extract copy node 
            copy = oldToCopy[curr]

            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]

            curr = curr.next
        
        return oldToCopy[head]

        