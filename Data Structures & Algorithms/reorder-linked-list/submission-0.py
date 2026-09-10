# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #the idea is to have two pointers, one at the end of the list and one at
        #the beginning, then placement will be front, end, front end ,front ,end 
        slow , fast = head, head.next # fast pointer will start 1 ahead for sake of odd
        while fast and fast.next: #keep looping until fast is null / reached end of list
            slow = slow.next
            fast = fast.next.next

        second = slow.next #second half of the list (slow is at the end of first half)
        slow.next = None #this splits the two lists
        prev = None
        while second: #while not null , we are now reversing this list
            nxt = second.next
            second.next = prev #point backwards
            prev = second
            second = nxt
        #at the end of this loop second will be null 
        #so the beginning of the second half will be prev node

        # merge the two halfs
        
        first, second = head, prev 

        while second: #second half can be larger than first half 
            nxt1, nxt2 = first.next, second.next
            first.next = second #pointer points to (last el (first el in reverse))
            second.next = nxt1 #pointer points to second el
            first = nxt1 # moves second el, then will point to scnd to last el
            second = nxt2 #moves to the next el, then will point to 3rd el 





