# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        p1 = head
        p2 = head
        
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p2 == p1:
                break
        
        if not p2 or not p2.next:
            return None
        p1 = head
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2