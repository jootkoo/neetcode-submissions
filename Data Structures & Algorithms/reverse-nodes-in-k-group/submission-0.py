# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            #create dummy node
            dummy = ListNode(0, head)
            groupPrev = dummy

            while True:
                kth = self.getKth(groupPrev, k)
                if not kth:
                    break
                groupNext = kth.next

                #reverse the group
                #if prev was none we would split the list
                prev, curr = kth.next, groupPrev.next #first node in group
                while curr != groupNext:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                tmp = groupPrev.next #stores the first node in group
                groupPrev.next = kth
                groupPrev = tmp
            return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr

    