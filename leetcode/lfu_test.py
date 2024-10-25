from collections import defaultdict 
class LinkedListNode:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def insterttail(self, node):
        if not self.tail:
            self.tail = node
    def removenode(self,node):
        if node is None:
            return
        if node.pre is not None:
            node.pre.next = node.next
        if node.next is not None:
            node.next.prev = node.pre
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
 

class lfu:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.frequencyMap = defaultdict(LinkedList)
        self.minFreq = 0
    def put(self, key, value):
        '''1. if capacity is 0 return errot 
            2. if the key in cache, get() the node and update the value
            3. if the size equal to the max capacity delete the node in cache and also deletet the head in frequencymap'''
        if self.capacity ==0:
            return 'the capacity is 0'
        if key in self.cache:
            self.get(key)
            self.cache[key].value = value
            return 
        if self.size==self.capacity:
            del 
        
    def get(self, key):
        '''1. if key is not in the cache, return -1
        2. because the freqrency changed we need to update the frequencyMap, 
        first delete the old frequency node, second add the node to new frequency likelist'''
        if key not in self.cache:
            return -1
        tempnode = self.cache[key]
        self.frequencyMap[tempnode.freq].removenode(tempnode)
        if self.frequencyMap[tempnode.freq].head is None:
            del self.frequencyMap[tempnode.freq]
            if self.minFreq == tempnode.freq:
                self.minFreq+=1
        self.cache[key].freq +=1
        self.frequencyMap[self.cache[key].freq].insterttail()
        return self.cache[key].value


