from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            res.append([])
            for i in range(len(queue)):
                curr = queue.popleft()
                res[level].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

        return res

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)

        level = 0

        while len(queue) > 0:
            level_vals = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_vals.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level_vals)
            level += 1

        return res
