class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val

            if not node.left and not node.right:
                return currSum == targetSum

            return (dfs(node.right, currSum)) or (dfs(node.left, currSum))

        return dfs(root, 0)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the current node is None, there's no path
        if not root:
            return False

        # Subtract the current node's value from the target sum
        targetSum -= root.val

        # If it's a leaf node, check if the remaining sum is zero
        if not root.left and not root.right:
            return targetSum == 0

        # Recursively check the left and right subtrees
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
