# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        first = second = temp
        
        for i in range(n):
            first = first.next
        
        while first.next != None:
            first = first.next
            second = second.next
        else:
            second.next = second.next.next
        
        return temp.next