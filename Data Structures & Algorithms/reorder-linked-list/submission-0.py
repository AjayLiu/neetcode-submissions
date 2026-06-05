# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Invert starting from half
        tail = None
        curr = slow
        prev = None            
        while curr:
            tail = curr
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while tail.next:
            headnxt = head.next
            tailnxt = tail.next

            head.next = tail
            tail.next = headnxt

            head = headnxt
            tail = tailnxt
