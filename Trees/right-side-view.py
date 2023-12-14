from collections import deque
from typing import List, Optional
from treenode import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        myQ = deque()
        myQ.append(root)
        ans = []

        while len(myQ) != 0:
            size = len(myQ)
            sub = []
            while size!=0:
                node = myQ.popleft()
                sub.append(node.val)
                if node.left != None:
                    myQ.append(node.left)
                
                if node.right != None:
                    myQ.append(node.right)
                
                size-=1
                if size == 0:
                    ans.append(sub[-1])
        
        return ans

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))
ans = Solution().rightSideView(root)
print(ans)