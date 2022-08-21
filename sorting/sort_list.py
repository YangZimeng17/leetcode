# 148. Sort List
# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        fast = head.next
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        
        left= self.sortList(head)
        right = self.sortList(start)
        
        return self.merge(left, right)
        
        
    def merge(self, left, right):
        if not left or not right:
            return left or right
        
        dummy = p = ListNode(0)
        
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
            
        p.next = left or right
        return dummy.next