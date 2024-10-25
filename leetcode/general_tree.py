from typing import *
from tree import Tree
root = Tree.build_regular_tree()

def preorder(root):
    result = []
    st = [root]
    while st:
        node = st.pop()
        if not node:
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            st.append(node)
            st.append(None)
        else:
            node = st.pop()
            result.append(node.val)
        
    return result

def inorder(root):
    result = []
    st = [root]
    while st:
        node = st.pop()
        if not node:
            if node.right:
                st.append(node.right)
            st.append(node)
            st.append(None)
            if node.left:
                st.append(node.left)
        else:
            








