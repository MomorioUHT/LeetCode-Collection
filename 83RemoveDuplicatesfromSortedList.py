# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur: #run until null
            while cur.next and cur.next.val == cur.val: #Check duplicates
                cur.next = cur.next.next #Skip duplicates val
            cur = cur.next
        return head