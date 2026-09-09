# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode()
        tail = dummy

        while list1 and list2: #runs while both are not None
            if list1.val > list2.val: #if the val is greater than list2
                tail.next = list2 #new list we are making .next = whole list 2
                list2 = list2.next #move the pointer up to the next one in the list
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        if list1: #not empty
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next #returns dummy.next to not include the None



            