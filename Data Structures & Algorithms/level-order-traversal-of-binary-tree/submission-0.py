# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        que = deque()
        que.append(root)
        res = []
        while que:
            tmp = []
            for i in range(len(que)):
                q = que.popleft()
                if q:
                    tmp.append(q.val)
                    que.append(q.left)
                    que.append(q.right)
            if tmp:
                res.append(tmp)
        return res