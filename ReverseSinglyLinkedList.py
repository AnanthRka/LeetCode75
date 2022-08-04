from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head:ListNode = None):
    if not head:
        return None
    
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

print(reverse([]))