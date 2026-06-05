# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # reverse list

        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        curr = head
        curr_2 = prev

        while curr_2:
            tmp1, tmp2 = curr.next, curr_2.next
            curr.next = curr_2
            curr_2.next = tmp1
            curr, curr_2 = tmp1, tmp2


