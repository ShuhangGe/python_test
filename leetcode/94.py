from typing import *
from tree import Tree
class TreeNode():
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None
# 94. Binary Tree Inorder Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # stack = []
        # results = []
        # cur = root
        # while cur or stack:
        #     if cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     else:
        #         cur = stack.pop()
        #         results.append(cur.val)
        #         cur = cur.right
        # return results
        
        if not root:
            return []
        stack = [root]
        results = []
        
        while stack:
            node = stack.pop()
            if node != None:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                results.append(node.val)
        return results
root = Tree.build_regular_tree()
solution = Solution()
print(solution.inorderTraversal(root))
