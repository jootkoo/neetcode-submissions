# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse the list
        #then remove node from there
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev #current node pointer points backwards
            prev = curr
            curr = nxt
        curr = prev
        start  = curr #need to mark the start of the list for re-reverse
        prev = None
        for i in range(n-1):
            prev = curr
            curr = curr.next
        if prev is None:
            start = curr.next 
        else:
            prev.next = curr.next #removes the node, unlinks it
        

        prev = None
        while start:
            nxt = start.next
            start.next = prev #current node pointer points backwards
            prev = start
            start = nxt
        
        return prev


        
            
            
