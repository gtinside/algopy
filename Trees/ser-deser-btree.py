from treenode import TreeNode

class Codec:

    def serialize(self, root):
        self.res = []
        self.dfsSer(root)
        return ",".join(self.res)
    
    def dfsSer(self, root):
        if root is None:
            self.res.append("N")
            return
        self.res.append(str(root.val))
        self.dfsSer(root.left)
        self.dfsSer(root.right)

    def deserialize(self, data):
        data = list(data.split(","))
        self.i = 0
        return self.dfsDeser(data)

    
    def dfsDeser(self, data):
        if self.i >=len(data):
            return None
        if data[self.i] == "N":
             self.i +=1
             return None
        
        node = TreeNode(int(data[self.i]))
        self.i+=1
        node.left = self.dfsDeser(data)
        node.right = self.dfsDeser(data)
        return node
        

root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
root1.right = TreeNode(3, TreeNode(6), TreeNode(7))

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root1))
print(ans)