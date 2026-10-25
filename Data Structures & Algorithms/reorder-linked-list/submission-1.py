# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # base case - list 3 or more node
        if not head or not head.next or not head.next.next:
            return 
        
        #1. Find middle part
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #2. reverse second broken half

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        back = prev
        front = head

        #3. Interleave
        while back:
            front_temp = front.next
            back_temp = back.next

            front.next = back
            back.next = front_temp

            front = front_temp
            back = back_temp
        
        
