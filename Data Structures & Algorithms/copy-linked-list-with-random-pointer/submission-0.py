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
        
        ran_hash = {}

        curr = head
        new_node_head = Node(curr.val)
        curr_new = new_node_head

        curr = curr.next

        while curr is not None:
            curr_new.next = Node(curr.val)
            curr_new = curr_new.next
            curr = curr.next

        curr_2 = head
        curr_copy = new_node_head
        while curr_2 is not None:
            if curr_2 not in ran_hash:
                ran_hash[curr_2] = curr_copy
            curr_2 = curr_2.next
            curr_copy = curr_copy.next
        
        curr_4 = head
        curr_5 = new_node_head

        while curr_4 is not None: 
            if curr_4.random: 
                curr_5.random = ran_hash[curr_4.random]
            else:
                curr_5.random = None
            curr_4 = curr_4.next
            curr_5 = curr_5.next
        
        return new_node_head



        