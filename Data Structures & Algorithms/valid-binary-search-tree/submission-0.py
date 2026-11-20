# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        que = deque([(root,float('-inf'),float('inf'))])
        while que:
            for i in range(len(que)):
                node,left,right = que.popleft()
                if not(left<node.val<right):
                    return False
                
                if node.left:
                    que.append((node.left,left,node.val))
                if node.right:
                    que.append((node.right,node.val,right))
        return True