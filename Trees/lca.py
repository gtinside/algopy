from treenode import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root, p, q)
    
    def lca(self,root, p, q):
        if root is None:
            return root
        
        if root.val == p.val or root.val == q.val:
            return root

        if root.val > p.val and root.val < q.val:
            return root
        
        if root.val < p.val and root.val > q.val:
            return root
        
        if root.val > p.val and root.val > q.val:
            return self.lca(root.left, p, q)
        
        return self.lca(root.right, p, q)


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Specify values for p and q
p = TreeNode(2)
q = TreeNode(4)

print(Solution().lowestCommonAncestor(root, p, q).val)