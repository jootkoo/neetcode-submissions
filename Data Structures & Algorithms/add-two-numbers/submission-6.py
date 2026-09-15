# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode(0) #initalize with dummy node
        new = dummy #set pointer 
        while curr1 and curr2: #while both are not empty
            total = curr1.val + curr2.val + carry #total value w carryover
            digit = total % 10
            curr = new #current pointer

            new = ListNode(digit) #initalize new node
            #carry counter 
            carry =  total // 10

            curr.next = new #move pointer to current node
            curr = curr.next #move pointer up
            curr1 = curr1.next #move down the list 
            curr2 = curr2.next
        #if curr1 not empty
        if curr1:
            curr = new
            while curr1:
                digit = (curr1.val + carry) % 10
                new = ListNode(digit)
                #reset carry counter
                carry =  (curr1.val + carry) // 10

                curr.next = new
                curr = curr.next
                curr1 = curr1.next
        #if curr2 not empty
        elif curr2:
            curr = new
            while curr2:
                digit = (curr2.val + carry) % 10
                new = ListNode(digit)
                #reset carry counter
                carry =  (curr2.val + carry) // 10

                curr.next = new
                curr = curr.next
                curr2 = curr2.next
        if carry > 0:
            curr = new
            new = ListNode(carry)
            curr.next = new
            curr = curr.next

        return dummy.next
                