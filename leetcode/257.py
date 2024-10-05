from typing import *
class TreeNode():
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack, path_st, result = [root], [str(root.val)], []

        while stack:
            cur = stack.pop()
            path = path_st.pop()
            print('stack: ',stack)
            # print('cur: ',cur)
            print('path: ',path)
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path + '->' + str(cur.left.val))

        return result
class Tree():
    def __init__(self) -> None:
        self.result_preorder = []
        self.result_inorder = []
    def preorder(self,root:TreeNode):
        if root is None:
            return 
        self.result_preorder.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root:TreeNode):
        if root is None:
            return 
        self.preorder(root.left)
        self.result_inorder.append(root.data)
        self.preorder(root.right)
    def build_tree(self, inorder: List[int], postorder: List[int])->TreeNode:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.build_tree(inorder[:index],postorder[:index])
        root.right = self.build_tree(inorder[index+1:],postorder[index:-1])
        return root
    def build_regular_tree(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        root = self.build_tree(inorder,postorder)
        print('        3\n 9     20\n 15   7 ')
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
    solution = Solution()
    print(solution.binaryTreePaths(root))