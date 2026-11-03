'''
This file implements the Node and BinaryTree classes.
These two classes are the building blocks for the BST, AVLTree, and Heap
data structures.
'''


class Node():
    '''
    Node data structure with assertion invariant checks.
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # NOTE: left should always be a Node or None
        self.right = right  # NOTE: right should always be a Node or None
        self.assert_invariants()

    def assert_invariants(self):
        '''
        Checks that children are Node instances or None.
        '''
        if self.left is not None:
            assert isinstance(self.left, Node), (
                f"left child must be a Node, got {type(self.left)}"
            )
        if self.right is not None:
            assert isinstance(self.right, Node), (
                f"right child must be a Node, got {type(self.right)}"
            )

    def __str__(self):
        '''
        Visualizes the node in the format: (value (left) (right))
        '''
        self.assert_invariants()
        out = '('
        out += str(self.value)
        if self.left:
            out += ' '
            out += str(self.left)
        if self.right:
            out += ' '
            out += str(self.right)
        out += ')'
        return out


class BinaryTree():
    '''
    Superclass for the BST, AVLTree, and Heap classes.
    '''

    def __init__(self, root=None):
        if root is not None:
            if isinstance(root, Node):
                self.root = root
            else:
                self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        if self.root is None:
            return '()'
        return str(self.root)

    def print_tree(self, traversal_type):
        '''
        Prints the tree nodes according to traversal_type.
        '''
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError(
                'Traversal type ' + str(traversal_type) + ' is not supported.'
            )

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def to_list(self, traversal_type):
        '''
        Returns tree nodes as a Python list according to traversal_type.
        '''
        if traversal_type == 'preorder':
            return self.preorder(self.root, [])
        elif traversal_type == 'inorder':
            return self.inorder(self.root, [])
        elif traversal_type == 'postorder':
            return self.postorder(self.root, [])
        else:
            raise ValueError(
                'Traversal type ' + str(traversal_type) + ' is not supported.'
            )

    def preorder(self, start, traversal):
        '''
        Preorder: Root -> Left -> Right
        '''
        if start:
            traversal.append(start.value)
            self.preorder(start.left, traversal)
            self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        '''
        Inorder: Left -> Root -> Right
        '''
        if start:
            self.inorder(start.left, traversal)
            traversal.append(start.value)
            self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        '''
        Postorde: Left -> Right -> Root
        '''
        if start:
            self.postorder(start.left, traversal)
            self.postorder(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def __len__(self):
        return BinaryTree.__len__helper(self.root)

    @staticmethod
    def __len__helper(node):
        if node is None:
            return 0
        total = 1
        if node.left:
            total += BinaryTree.__len__helper(node.left)
        if node.right:
            total += BinaryTree.__len__helper(node.right)
        return total

    def height:
