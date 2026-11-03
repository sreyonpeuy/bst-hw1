'''
This file implements the Binary Search Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    Binary Search Tree subclass inheriting from BinaryTree.
    '''

    def __init__(self, xs=None):
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        '''
        Checks whether the BST properties are satisfied in O(n) time.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node, min_val=float('-inf'), max_val=float('inf')):
        '''
        Validates BST property in O(n) using upper and lower bounds.
        '''
        if node is None:
            return True

        if not (min_val <= node.value <= max_val):
            return False

        if not BST._is_bst_satisfied(node.left, min_val, node.value):
            return False

        if not BST._is_bst_satisfied(node.right, node.value, max_val):
            return False

        return True

    def insert(self, value):
        '''
        Inserts value into the BST.
        '''
        if self.root is None:
            self.root = Node(value)
        else:
            BST._insert(value, self.root)

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                BST._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                BST._insert(value, node.right)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element into the tree.
        '''
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.
        '''
        if self.root is None:
            return False
        return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return BST._find(value, node.left)
        else:
            return BST._find(value, node.right)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        assert node is not None
        if node.left is None:
            return node.value
        return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST if present.
        '''
        self.root = BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):
        if node is None:
            return None

        if value < node.value:
            node.left = BST._remove(value, node.left)
        elif value > node.value:
            node.right = BST._remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = BST._find_smallest(node.right)
                node.value = successor
                node.right = BST._remove(successor, node.right)

        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element from the tree.
        '''
        for x in xs:
            self.remove(x)
