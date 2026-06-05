# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_len = 0
        curr = head

        while curr:
            total_len+=1
            curr = curr.next
        
        pos = total_len - n

        if pos == 0:
            return head.next

        tmp = head
        
        for i in range(total_len - 1):
            if (i+1) == pos:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
        return head

