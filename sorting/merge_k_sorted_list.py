# 23. Merge k Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)

    def mergeLists(self, lists, s, e):
        if s == e:
            return lists[s]
        mid = s + (e - s) // 2
        left = self.mergeLists(lists, s, mid)
        right = self.mergeLists(lists, mid + 1, e)
        return self.merge(left, right)

    @staticmethod
    def merge(left, right):
        head = ListNode(-1)
        temp = head
        while left != None and right != None:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        while left != None:
            temp.next = left
            left = left.next
            temp = temp.next
        while right != None:
            temp.next = right
            right = right.next
            temp = temp.next
        return head.next