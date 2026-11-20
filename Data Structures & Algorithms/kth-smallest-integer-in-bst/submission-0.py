# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        count = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            count += 1
            cur = stack.pop()
            if count == k:
                return cur.val
            
            cur = cur.right
            
