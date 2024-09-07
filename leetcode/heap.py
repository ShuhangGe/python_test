from typing import *
class Heap():
    def __init__(self):
        self.heap = []
    def push(self, data:int) -> int:
        self.heap.append(data)
        self.up(len(self.heap)-1)
    def pop(self) -> int:
        if len(self.heap)==0:
            return None
        result = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.down(0)
        return result
    def up(self, index:int) -> None:
        if index <= 0:
            return 
        parent = (index-1)//2
        if self.heap[index] < parent:
            self.swap(parent, index)
            self.up(parent)
    def swap(self, parent:int, child:int)->None:
        self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
    def down(self, index):
        left = 2*index +1
        right = 2*index +2
        smallest = index
        if left<len(self.heap) and self.heap[left]<self.heap[index]:
            smallest = left
        if right<len(self.heap) and self.heap[right]<self.heap[index]:
            smallest = right     
        if smallest != index:
            self.swap(index,smallest)
            self.down(smallest)
    def insert(self, data):
        self.push(data)
    def extract_min(self):
        return self.pop()
    def get_min(self):
        return self.heap[0]
    def size(self):
        return len(self.heap)
    def is_empty(self):
        return len(self.heap) == 0
heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(10)
heap.insert(1)
heap.insert(4)
heap.insert(2)
print(heap.extract_min())
print(heap.get_min())
print(heap.size())
print(heap.is_empty())