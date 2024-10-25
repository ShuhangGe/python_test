# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
from typing import *
from tree import Tree
root_o = Tree.build_regular_tree()
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        stack = collections.deque()
        stack.append(root)
        res = []
        while stack:
            cur_node = stack.popleft()
            if cur_node:
                res.append(cur_node.val)
                stack.append(cur_node.left)
                stack.append(cur_node.right)
            else:
                res.append("null")
        print('res: ',res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        root = TreeNode(data[0])
        queue = collections.deque()
        queue.append(root)
        idx = 1
        data_length = len(data)
        while queue:
            cur_node = queue.popleft()
            if idx<data_length and data[idx] != "null":
                cur_node.left = TreeNode(data[idx])
                queue.append(cur_node.left)
            idx+=1
            if idx<data_length and data[idx]!= "null":
                cur_node.right = TreeNode(data[idx])
                queue.append(cur_node.right)
            idx+=1
        return root

    

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root_o))

print('ser.serialize(ans): ',ser.serialize(ans))