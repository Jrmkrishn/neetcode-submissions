# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        maps = {}
        cur = head
        i = 0
        while cur:
            maps[i] = cur 
            cur = cur.next
            i += 1
        idx = i - n
        if idx == 0:
            head = head.next
        tmp = maps[idx].next
        if idx - 1 >= 0:
            maps[idx - 1].next = tmp
        return head