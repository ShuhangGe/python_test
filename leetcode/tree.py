from typing import *

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def iterativePreorder(root:Node)->list:
    if root is None:
        return 
    result = []
    stack = []
    stack.append(root)
    while stack:
        point = stack.pop()
        result.append(point.val)
        if point.right is not None:
            stack.append(point.right)
        if point.left is not None:
            stack.append(point.left)
    return result


def iterativeInorder(root:Node)->list:
    if root is None:
        return 
    current  = root
    result = []
    stack = []
    stack.append(root)
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            result.append(current.val)
            current = current.right
        else:
            break
    return result
            
        
def iterativePostorder_2stack(root:Node)->list:
    '''postorder is left, right, root, so the need to save in stack as root, right, left.
    "Use two stacks to traverse the tree. First, push the root node into the first stack. Then, 
    pop the node from the first stack and push it into the second stack. Next, push the left and right
    children of the node into the first stack. Continue this process, ensuring that when popping nodes
    from the first stack, they are pushed into the second stack in the order of right child first, 
    followed by the left child.
    '''
    if root is None:
        return 
    result = []
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        result.append(node.val)
    return result
    
def iterativePreorder2_postorder(root:Node)->list:
    stack = [root]
    while stack:
        cur = stack.pop()
        cur.left, cur.right = cur.right, cur.left
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    if root is None:
        return 
    result = []
    stack = []
    stack.append(root)
    while stack:
        point = stack.pop()
        result.append(point.val)
        if point.right is not None:
            stack.append(point.right)
        if point.left is not None:
            stack.append(point.left)
    result.reverse()
    return result

def iterativePostorder_1stack1(root): 
    ''''''
    ans = []
    if root is None:
        return 
    stack = []
    while True:
        print('stack0:',[i.val for i in stack])
        print('ans: ', ans)
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root = root.left
            print('stack1:',[i.val for i in stack])
            print('ans: ', ans)
        root = stack.pop()
        print('stack2:',[i.val for i in stack])
        print('ans: ', ans)
        if root.right is not None and len(stack) > 0 and stack[-1] == root.right:
            # if (len(stack)>=0 and stack[-1]==root.right):
                stack.pop()
                stack.append(root)
                root = root.right
                print('stack3:',[i.val for i in stack])
                print('ans: ', ans)
        else:
            ans.append(root.val)
            root = None
            print('stack4:',[i.val for i in stack])
            print('ans: ', ans)
        if len(stack)<=0:
            break
    return ans

def iterativePostorder_1stack2(root): 
    ans = []
    if root is None:
        return 
    stack = []
    while True:
        while root:
            stack.append(root)
            stack.append(root)
            root = root.left
        if len(stack):
            return ans
        root = stack.pop()

        if len(stack)>0 and stack[-1]==root:
            root = root.right
        else:
            ans.append(root.val)
            root = None
        
def iterativePostorder_1stack3(root): 
    ans = []
    if root is None:
        return 
    stack = [root]
    pre = None
    while stack:
        cur = stack[-1]
        if pre == None or pre.left ==cur or pre.right == cur:
            if cur.left:
                stack.append(cur.left)
            elif cur.right:
                stack.append(cur.right)
            else:
                ans.append(cur.val)
                stack.pop()
        elif pre == cur.left:
            if cur.right:
                stack.append(cur.right)
            else:
                ans.append(cur.val)
                stack.pop()
        else:
            ans.append(cur.val)
            stack.pop()
        pre = cur
        
    return ans


class Tree():
    def __init__(self) -> None:
        self.result_preorder = []
        self.result_inorder = []
    def preorder(self,root:Node):
        if root is None:
            return 
        self.result_preorder.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root:Node):
        if root is None:
            return 
        self.preorder(root.left)
        self.result_inorder.append(root.val)
        self.preorder(root.right)
    @classmethod
    def build_tree(self, inorder: List[int], postorder: List[int])->Node:
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        index = inorder.index(root_val)
        root = Node(root_val)
        root.left = self.build_tree(inorder[:index],postorder[:index])
        root.right = self.build_tree(inorder[index+1:],postorder[index:-1])
        return root
    @classmethod
    def build_regular_tree(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        root = self.build_tree(inorder,postorder)
        print('tree example:\n        3\n    9     20\n        15   7 ')
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
    # print(root)
    # print(iterativePreorder(root))
    # print(iterativePostorder_2stack(root))
    # print(iterativePostorder_1stack1(root))
    print(iterativePostorder_1stack3(root))
    print(iterativePreorder(root))
    print(iterativePreorder2_postorder(root))