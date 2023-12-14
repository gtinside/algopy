from typing import List, Optional
from treenode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.inOrder(root)
        return self.arr[k - 1]

    def inOrder(self, root):
        if root is None:
            return
        
        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)


root = TreeNode(5)
root.left = TreeNode(2, TreeNode(1), TreeNode(4))
root.right = TreeNode(10, TreeNode(6), TreeNode(11))
ans = Solution().kthSmallest(root, 4)
print(ans)