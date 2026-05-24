class Node:
    def __init__(self, key = -1, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict() 
        
        # Least Recent (oldest) -> ... -> Most Recent (newest)
        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _rm (self, node: Node) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache[key].val

        # Reinsert
        self._rm(self.cache[key])

        new_node = Node(key, val, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.cache[key] = new_node

        return val

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self._rm(self.cache[key])
        else:
            self.capacity -= 1
        
        new_node = Node(key, value, self.tail.prev, self.tail)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.cache[key] = new_node

        # Remove head if necessary
        if self.capacity < 0:
            oldest = self.head.next
            self._rm(oldest)
            del self.cache[oldest.key] 
            self.capacity += 1

        
        
