class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class lru_cache():
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key):
        '''return -1 if not '''
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move2head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move2head(node)
        else:
            node = Node(key, value)
            self.cache[key] =node
            self.add2head(node)
            self.size+=1
            if self.size > self.capacity:
                removed_node = self.remove_tail
                del self.cache[removed_node.key]
                self.size-=1
    def remove_tail(self):
        node = self.tail.prev
        self.delete_node(node)
        return node
    def move2head(self,node):
        self.delete_node(node)
        self.add2head(node)
    def delete_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def add2head(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

        
