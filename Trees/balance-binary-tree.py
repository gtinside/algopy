from typing import Optional
from treenode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = self.check(root)
        if ans == float("inf"):
            return False
        
        return True
    
    def check(self, root):
        if root == None:
            return 0
        
        l = self.check(root.left)
        r = self.check(root.right)

        if l == float("inf") or r == float("inf") or abs(l - r) > 1:
            return float("inf")
        
        return 1 + max(l, r)


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

solution = Solution()
print(solution.isBalanced(root))

        