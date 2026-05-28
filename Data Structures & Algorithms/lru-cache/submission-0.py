class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left

#insert node to become mru
    def insert(self, node):
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node
        node.next = self.right

        self.right.prev = node

#remove node
    def remove(self, node):
        prev_node = node.prev
        nxt_node = node.next

        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        self.remove(node)
        self.insert(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            
            del self.cache[lru.key]

            
 
        
