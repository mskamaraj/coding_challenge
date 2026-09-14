class TreeNode:
    def __init__(self, data:int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __insert_using_while_loop(self, data:int):
        newNode = TreeNode(data)
        if self.root == None:
            self.root = newNode
            return

        node = self.root
        while node != None:
            if node.data<data:
                if node.right == None:
                    node.right = newNode
                    return
                node = node.right
            else:
                if node.left == None:
                    node.left = newNode
                else:
                    node = node.left

    def __inser_using_recursion(self, node:TreeNode, data:int):
        if node == None:
            return TreeNode(data)
        if data<node.data:
            node.left = self.__inser_using_recursion(node.left, data)
        else:
            node.right = self.__inser_using_recursion(node.right, data)
        return node

    def insert(self, data:int):
        self.root = self.__inser_using_recursion(self.root, data)

    def __inorder_traverse(self, node:TreeNode):
        if node:
            self.__inorder_traverse(node.left)
            print(node.data)
            self.__inorder_traverse(node.right)

    def inorder_traverse(self):
        self.__inorder_traverse(self.root)


tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.inorder_traverse()

