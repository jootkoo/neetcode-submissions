# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #starts with left child first, self.maxDepth(root.left) goes first
        #then recursively goes down, going left until reaches none, then goes back
        #to most recent paused recursive call then goes right, then goes left until same

        #adds 1 to every real recursive call, not when it goes back to the paused

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
