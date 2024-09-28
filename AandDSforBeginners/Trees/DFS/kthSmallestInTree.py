class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, stack = [], []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res[k - 1]
