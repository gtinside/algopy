from treenode import TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self.getMax(root)
        return self.ans
    

    def getMax(self, root):
        if root is None:
            return 0
        
        left = self.getMax(root.left)
        right = self.getMax(root.right)

        if left <0:
            left = 0
        
        if right < 0:
            right = 0

        self.ans = max(self.ans, root.val + left + right)
        return root.val + max(left, right)

root = TreeNode(10)
root.left = TreeNode(5, TreeNode(4), TreeNode(5))
root.right = TreeNode(20, TreeNode(30), TreeNode(40))
print(Solution().maxPathSum(root))
        