from typing import *

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self) -> None:
        self.result_preorder = []
        self.result_inorder = []
    def preorder(self,root:Node):
        if root is None:
            return 
        self.result_preorder.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root:Node):
        if root is None:
            return 
        self.preorder(root.left)
        self.result_inorder.append(root.data)
        self.preorder(root.right)
    def build_tree(self, inorder: List[int], postorder: List[int])->Node:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        index = inorder.index(root_val)
        root = Node(root_val)
        root.left = self.build_tree(inorder[:index],postorder[:index])
        root.right = self.build_tree(inorder[index+1:],postorder[index:-1])
        return root

if __name__ == '__main__':
    tree = Tree()
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    '''  
        3
    9     20
        15   7 
    '''
    root = tree.build_tree(inorder,postorder)