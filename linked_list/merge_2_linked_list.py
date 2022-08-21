# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val < list2.val:
            head = ListNode(list1.val)
            temp = head
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            temp = head
            list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
        
            temp = temp.next

        while list1 != None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        
        while list2 != None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
                
        return head