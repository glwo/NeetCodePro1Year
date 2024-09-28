# Recursion
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], arr = None) -> List[int]:
        if arr is None:
            arr = []

        if root:
            self.inorderTraversal(root.left, arr)
            arr.append(root.val)
            self.inorderTraversal(root.right, arr)

        return arr


# Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative
        res, stack = [], []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
