from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            right = None

            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    right = curr
                    q.append(curr.left)
                    q.append(curr.right)

            if right:
                res.append(right.val)

        return res

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        if root:
            q.append(root)

        level = 0

        while len(q) > 0:
            right = None
            if level >= len(res) - 1:
                res.append(0)
            for i in range(len(q)):
                curr = q.popleft()
                right = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res[level] = right.val
            level += 1

        return res
