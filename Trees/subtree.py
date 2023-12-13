from typing import Optional
from treenode import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True
        
        # check if subroot is subtree of root, or a left subtree or right subtree
        checkFromRoot = self.checkIfSubtree(root, subRoot)
        checkFromLeft = self.isSubtree(root.left, subRoot)
        checkFromRight = self.isSubtree(root.right, subRoot)

        return checkFromRoot or checkFromLeft or checkFromRight
    

    # Check if subRoot is subtree of root
    def checkIfSubtree(self, root, subRoot):
        if subRoot is None and root is None:
            return True
        
        if subRoot is None or root is None or root.val != subRoot.val:
            return False
        
        # values are same, lets dig deep
        return self.checkIfSubtree(root.left, subRoot.left) and self.checkIfSubtree(root.right, subRoot.right)

root = TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, 
                                                    TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(2))))))))))))))))))))))))

subRoot = TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(1, None, TreeNode(2))))))))))))))))))))))))))))))))))))))))))

solution = Solution()
print(solution.isSubtree(root, subRoot))