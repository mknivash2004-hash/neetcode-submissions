# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        cur1 = head
        cur2 = prev
        while cur2:
            tmp1,tmp2 = cur1.next,cur2.next
            cur1.next = cur2
            cur2.next = tmp1
            cur1 = tmp1
            cur2 = tmp2
        