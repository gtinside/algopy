from typing import Optional
from treenode import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)

    def depth(self, root):
        if root == None:
            return 0
        l = self.depth(root.left)
        h = self.depth(root.right)
        return 1 + max(l,h)


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

solution = Solution()
max_depth = solution.maxDepth(root)

print(max_depth)   