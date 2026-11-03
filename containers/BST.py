'''
This file implements the Binary Search Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree file.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a subclass of BinaryTree.
    That means that the BST class "inherits" all of the methods from BinaryTree,
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        if xs is not None:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of BST will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node, min_val=float('-inf'), max_val=float('inf')):
        '''
        Uses _find_largest on the left subtree and _find_smallest on the right subtree
        to verify that ALL nodes in the left subtree are <= node.value, and ALL
        nodes in the right subtree are >= node.value, while recursing down the tree.
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
        '''
        Helper method that traverses down the tree to place value at an empty leaf spot.
        '''
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
        # If value == node.value, standard BSTs ignore duplicates

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        '''
        for x in xs:
            self.insert(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
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
        '''
        Recursive helper to search for a value in O(h) time.
        '''
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
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        This is a helper function for find_smallest and not intended to be called directly by the user.
        '''
        assert node is not None
        if node.left is None:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.
        '''
        if self.root is None:
            raise ValueError('Nothing in tree')
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        '''
        Helper function to find the maximum element by traversing rightmost children.
        '''
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.
        '''
        self.root = BST._remove(value, self.root)

    @staticmethod
    def _remove(value, node):
        '''
        Recursive helper to delete a value and restructure subtrees:
        - Case 0: Node has 0 children -> return None
        - Case 1: Node has 1 child -> return that child
        - Case 2: Node has 2 children -> replace node value with in-order successor
                  (smallest in right subtree) and recursively remove successor.
        '''
        if node is None:
            return None

        if value < node.value:
            node.left = BST._remove(value, node.left)
        elif value > node.value:
            node.right = BST._remove(value, node.right)
        else:
            # Found node to delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # 2 children: replace with successor value
                successor_val = BST._find_smallest(node.right)
                node.value = successor_val
                node.right = BST._remove(successor_val, node.right)

        return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.
        '''
        for x in xs:
            self.remove(x)
