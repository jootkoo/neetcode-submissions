# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #idea is to merge sort linked lists
        if not lists or len(lists) == 0:
            return None
        #take pairs of linked lists and merge them each time until 1 left remaining
        while len(lists) > 1:
            mergedList = [] #put in new list

            for i in range(0, len(lists), 2): #merge sort, pairs so increments of 2 
                l1 = lists[i] 
                l2 = lists[i + 1] if (i+1) < len(lists) else None #check if in bounds
                mergedList.append(self.mergeList(l1, l2)) #self becauese in same class
            lists = mergedList #reset lists to new list
        return lists[0]


    def mergeList(self, l1, l2):  #merge sort
        dummy = ListNode() #dummy node is already created in node class, val = 0
        tail = dummy 

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 #place tail at start
                l1 = l1.next #move up list
            else:
                tail.next = l2 
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next #dummy.next bc first val is 0 





            