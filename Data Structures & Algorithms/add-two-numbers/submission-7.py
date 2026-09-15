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
        while curr1 or curr2 or carry: #while lists are not empty, carry is not 0 
            if curr1 and curr2:
                total = curr1.val + curr2.val + carry #total value w carryover
            elif curr1 and not curr2:
                total = curr1.val + carry
            elif curr2 and not curr1:
                total = curr2.val + carry
            else:
                total = carry
            digit = total % 10
            curr = new #current pointer

            new = ListNode(digit) #initalize new node
            #carry counter 
            carry =  total // 10

            curr.next = new #move pointer to current node
            curr = curr.next #move pointer up
            if curr1:
                curr1 = curr1.next #move down the list
            if curr2:
                curr2 = curr2.next
        return dummy.next
                