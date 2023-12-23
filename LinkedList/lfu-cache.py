from collections import defaultdict
class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, self.head, None)
        self.head.next = self.tail
        self.size = 0
    
    def insertToHead(self, node):
        curr = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = curr
        curr.prev = node
        self.size += 1
    
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def deleteFromTail(self):
        node_to_del = self.tail.prev
        node_to_del.prev.next = self.tail
        self.tail.prev = node_to_del.prev
        node_to_del.next = None
        self.size -= 1
        return node_to_del.key


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freqList = dict()
        self.keyValue = dict()
        self.keyFreq = defaultdict(int)
        self.freqDLL = defaultdict(DLL)
        

    def get(self, key: int) -> int:
        if key not in self.keyValue:
            return -1
        
        node = self.keyValue[key]
        old_freq =  self.keyFreq[node.key]
        new_freq = old_freq + 1
        self.freqDLL[old_freq].deleteNode(node)
        if self.freqDLL[old_freq].size == 0:
            self.freqDLL.pop(old_freq)
        self.freqDLL[new_freq].insertToHead(node)
        self.keyFreq[node.key] = new_freq

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keyValue:
            node = self.keyValue[key]
            node.value = value
            old_freq =  self.keyFreq[key]
            new_freq = old_freq + 1
            self.freqDLL[old_freq].deleteNode(node)
            if self.freqDLL[old_freq].size == 0:
                self.freqDLL.pop(old_freq)
            self.freqDLL[new_freq].insertToHead(node)
            self.keyFreq[key] = new_freq
        else:
            if len(self.keyValue) == self.capacity:
                # delete
                lowest_freq = list(sorted(self.freqDLL.keys()))[0]
                dll = self.freqDLL[lowest_freq]
                deleted_key = dll.deleteFromTail()
                print(deleted_key)
                if dll.size == 0:
                    self.freqDLL.pop(lowest_freq)
                self.keyValue.pop(deleted_key)
                self.keyFreq.pop(deleted_key)
            # insert
            node = Node(key, value)
            self.keyValue[key] = node
            self.keyFreq[key] = 1
            self.freqDLL[1].insertToHead(node)
        


lfu = LFUCache(2)
lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1))      # return 1
                 # cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 # cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2))      # return -1 (not found)
print(lfu.get(3))      # return 3
                 # cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 # cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1))      # return -1 (not found)
print(lfu.get(3))      # return 3
                 # cache=[3,4], cnt(4)=1, cnt(3)=3
print(lfu.get(4))      # return 4
                 # cache=[4,3], cnt(4)=2, cnt(3)=3
