from typing import List, Optional
from treenode import TreeNode

class Solution:
     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        rootIndex = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:rootIndex + 1], inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex + 1:], inorder[rootIndex + 1:])  

        return root

'''
 preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

'''