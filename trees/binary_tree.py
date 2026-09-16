from tree_node import TreeNode

class BinaryTree:
    def __init__(self, data:list=None):
        self.root = None
        if data:
            for item in data:
                self.insert(item)

    def insert(self, data:int):
        def insert_node(node:TreeNode, data:int):
            if node == None:
                return TreeNode(data)
            if data<node.data:
                node.left = insert_node(node.left, data)
            else:
                node.right = insert_node(node.right, data)
            return node
        self.root = insert_node(self.root, data)

    def insert_list(self, data:list):
        for item in data:
            self.insert(item)

    def inorder_traversal(self):
        list = []
        def inorder(node:TreeNode):
            if node:
                inorder(node.left)
                list.append(node.data)
                inorder(node.right)
        inorder(self.root)
        return list

    def inorder_traversal_stack(self):
        result = []
        stack = []
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.data)
            node = node.right
        return result

    def preorder_traversal_stack_v1(self):
        result = []
        stack = []
        node = self.root
        while stack or node:
            while node:
                result.append(node.data)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result
    
    def preorder_traversal_stack_v2(self):
            result = []
            stack = [self.root]
            while stack:
                node = stack.pop()
                result.append(node.data)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return result

    def postorder_traversal_stack_v1(self):
        result = []
        stack1 = [self.root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            result.append(node.data)
        return result

    def postorder_traversal_stack_v2(self):
        result = []
        stack = []
        last_visited = None
        node = self.root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    node = peek_node.right
                else:
                    result.append(peek_node.data)
                    last_visited = stack.pop()
        return result

        
    def preorder_traversal(self):
        list = []
        def preorder(node:TreeNode):
            if node:
                list.append(node.data)
                preorder(node.left)
                preorder(node.right)
        preorder(self.root)
        return list

    def postorder_traversal(self):
        list = []
        def postorder(node:TreeNode):
            if node:
                postorder(node.left)
                postorder(node.right)
                list.append(node.data)
        postorder(self.root)
        return list
       

print("Binary Tree Example:")
tree = BinaryTree([5, 3, 7, 2, 4, 6, 8])
print("Inorder Traversal:", tree.inorder_traversal())
print("Preorder Traversal:", tree.preorder_traversal())
print("Postorder Traversal:", tree.postorder_traversal())
print("Inorder Traversal (Stack):", tree.inorder_traversal_stack())
print("Preorder Traversal (Stack) V1:", tree.preorder_traversal_stack_v1())    
print("Preorder Traversal (Stack) V2:", tree.preorder_traversal_stack_v2())
print("Postorder Traversal (Stack) V1:", tree.postorder_traversal_stack_v1())
print("Postorder Traversal (Stack) V2:", tree.postorder_traversal_stack_v2())