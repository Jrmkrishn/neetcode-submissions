class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
        self.head, self.tail =  Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.nxt = nxt.prev = node
        node.prev = prev
        node.nxt = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        self.count += 1
        if self.count > self.capacity:
            lru = self.head.nxt
            self.remove(lru)
            print(lru.key in self.cache)
            del self.cache[lru.key]



        
