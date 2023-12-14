from treenode import TreeNode
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkIfValid(root, float("-inf"), float("inf"))
        
    
    def checkIfValid(self, root, leftMax, rightMax):
        if root is None:
            return True
        
        if root.val <= leftMax or root.val >= rightMax:
            return False
        
        return self.checkIfValid(root.left, leftMax, root.val) and self.checkIfValid(root.right, root.val, rightMax)


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))
ans = Solution().isValidBST(root)
print(ans)