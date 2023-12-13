from typing import Optional
from treenode import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)
        
    def invert(self, root):
        if root == None:
            return None
        temp = root.left
        root.left = self.invert(root.right)
        root.right = self.invert(temp)
        return root




import unittest

class TestSolution(unittest.TestCase):
    def test_invertTree(self):
        # Create a sample binary tree
        #     1
        #    / \
        #   2   3
        #  / \ / \
        # 4  5 6  7
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3, TreeNode(6), TreeNode(7))

        solution = Solution()
        inverted_root = solution.invertTree(root)

        # Check if the tree is inverted correctly
        #     1
        #    / \
        #   3   2
        #  / \ / \
        # 7  6 5  4
        self.assertEqual(inverted_root.val, 1)
        self.assertEqual(inverted_root.left.val, 3)
        self.assertEqual(inverted_root.right.val, 2)
        self.assertEqual(inverted_root.left.left.val, 7)
        self.assertEqual(inverted_root.left.right.val, 6)
        self.assertEqual(inverted_root.right.left.val, 5)
        self.assertEqual(inverted_root.right.right.val, 4)

if __name__ == '__main__':
    unittest.main()



