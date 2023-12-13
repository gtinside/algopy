from typing import Optional
from treenode import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.checkIfSame(p,q)
    
    def checkIfSame(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val != q.val:
            return False
        else:
            return self.checkIfSame(p.left, q.left) and self.checkIfSame(p.right, q.right)



root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
root1.right = TreeNode(3, TreeNode(6), TreeNode(7))

root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(4), TreeNode(5))
root2.right = TreeNode(3, TreeNode(6), TreeNode(7))

root3 = TreeNode(1)
root3.left = TreeNode(2, TreeNode(4), None)
root3.right = TreeNode(3, TreeNode(6), TreeNode(7))

print(Solution().isSameTree(root1, root2))

print(Solution().isSameTree(root1, root3))




