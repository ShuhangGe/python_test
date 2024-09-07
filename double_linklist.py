class node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addAtTail(self, data):
        if not self.head:
            self.head = node(data)
            self.tail = self.head
        else:
            self.tail.next = node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def get(self, index: int) -> int:
        if index<=0 or not self.head:
            return -1
        curr_node = self.head
        for _ in range(index-1):
            if curr_node.next is None:
                return -1
            curr_node = curr_node.next
        return curr_node.data

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = node(val)
            self.tail  = node(val)
        else:
            new_node = node(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 1:
            self.head = node(val)
            self.tail = self.head
        else:
            cur_node = self.head
            for _ in range(index-1):
                if cur_node.next is None:
                    return -1
                cur_node = cur_node.next
            new_node = node(val)
            cur_node.prev.next = new_node
            new_node.prev = cur_node.prev
            new_node.next = cur_node
            cur_node.prev = new_node
        


    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return -1
        cur_node = self.head
        if index ==1:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                if cur_node.next is None:
                    return -1
                cur_node = cur_node.next
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
        
        

makelist = MyLinkedList()
makelist.addAtHead(1)
makelist.addAtTail(1)
makelist.addAtIndex(1,1)
print(makelist.head.next.data)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)