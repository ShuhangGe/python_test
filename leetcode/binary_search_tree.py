from typing import *
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def get(self, root:Node, value:int) -> Node:
        if root is None or root.data == value:
            return root
        if value>root.data:
            return self.get(root.left,value)
        return self.get(root.right,value)
