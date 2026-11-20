# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que = collections.deque()
        que.append(root)
        result = []

        while que:
            lst = []
            for i in range(len(que)):
                node = que.popleft()
                if node:
                    lst.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if lst:
                result.append(lst)

        return result