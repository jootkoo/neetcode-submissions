# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #if never reaches null then has cycle
        #idea is to add NODES to the hashset for reference
        # OR use tortoise and hare method where there are 2 pointers
        #1 slow 1 fast, eventually the fast will catch the slow if no end otherwise null
        hashset = set()
        curr = head

        while curr:
            if curr in hashset:
                return True
            else:
                hashset.add(curr)
                curr = curr.next
        return False
