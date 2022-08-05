class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    if head.next is None:
        return head
    curr = head
    l = 0
    while curr:
        l+=1
        curr = curr.next
    
    middle = l//2 + 1
    curr = head
    for i in range(middle +1 ):
        curr = curr.next
    return curr

print(middleNode([1,2,3,4,5,6]))