# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create dummy node to start at 0 
        #use two pointers method
        #use fast and slow pointer to get to the end of the list 
        #the slow pointer will end up one before the fast
        #the fast will move up n times and then slowly move up till the end of the list
        #in sequence, the slow pointer will move as the fast moves
        #then the slow pointer will end up right before the nth node
        dummy = ListNode(0, head) #create new list with 0 at the start
        slow = dummy #have slow as the first element(0)
        fast = head
        
        for i in range(n): #move fast pointer up n elements
            fast = fast.next
        while fast: #keep going until its at the end of the list
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next #skip node
        return dummy.next



