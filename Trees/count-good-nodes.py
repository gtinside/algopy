from treenode import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.count(root, root.val)

        return self.ans
    
    def count(self, root, maxVal):
        if root is None:
            return
        
        if root.val >= maxVal:
            self.ans += 1
            maxVal = root.val
        
        self.count(root.left, maxVal)
        self.count(root.right, maxVal)

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))
ans = Solution().goodNodes(root)
print(ans)