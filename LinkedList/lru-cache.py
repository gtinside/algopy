class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, None, None)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.myDict = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.myDict:
            return -1
        
        node = self.myDict[key]
        self.removeFromList(node)
        self.insertToHead(node)
        return node.value
        
        '''
        dict =  {1,5} {1,2}
        
        head (1,2) (1,5) tail
        
        '''

    def put(self, key: int, value: int) -> None:
        if key in self.myDict:
            node = self.myDict[key]
            node.value = value
            self.removeFromList(node)
            self.insertToHead(node)
            return

        if len(self.myDict) == self.capacity:
            k = self.removeFromTail()
            self.myDict.pop(k)
        node = Node(key, value, None, None)
        self.myDict[key] = node
        self.insertToHead(node)

    
    def insertToHead(self, node):
        existing = self.head.next
        self.head.next = node
        
        node.next = existing
        node.prev = self.head
        existing.prev = node
    
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def removeFromTail(self):
        existing = self.tail.prev
        self.tail.prev = existing.prev
        existing.prev.next = self.tail
        return existing.key
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)   
lRUCache.put(3, 3)
lRUCache.get(2);   
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))    
print(lRUCache.get(4))