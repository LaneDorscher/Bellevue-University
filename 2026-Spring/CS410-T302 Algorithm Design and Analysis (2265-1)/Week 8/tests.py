from week8_assignment import *
import copy

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def is_key_in_bst(root, key):
    if not root:
        return False
    if root.val == key:
        return True
    elif root.val < key:
        return is_key_in_bst(root.right, key)
    else:
        return is_key_in_bst(root.left, key)


def test_insert_bst():
    root1 = TreeNode(50)
    root1.left = TreeNode(30)
    root1.right = TreeNode(70)

    root2 = TreeNode(40)

    root3 = TreeNode(20)
    root3.right = TreeNode(30)

    cases = [
        (root1, 20, True),  # Test 1
        (root1, 80, True),  # Test 2
        (root1, 45, True),  # Test 3
        (root2, 10, True),  # Test 4
        (root2, 50, True),  # Test 5
        (root3, 10, True),  # Test 6
        (root3, 25, True),  # Test 7
        (None, 10, True),  # Test 8
        (root1, 55, True),  # Test 9
        (root2, 45, True)  # Test 10
    ]

    return [(root, key, expected) for root, key, expected in cases]

def contains_key(root, key):
    """
    Helper function to check if the tree with the given root contains the key.
    """
    if root is None:
        return False
    if root.val == key:
        return True
    elif key < root.val:
        return contains_key(root.left, key)
    else:
        return contains_key(root.right, key)


def test_find_max_heap():
    cases = [
        ([10, 5, 3, 2, 4], 10), # Test 11
        ([15, 14, 10, 8, 7, 9, 3, 2, 4], 15), # Test 12
        ([1], 1), # Test 13
        ([50, 30, 10, 20], 50), # Test 14
        ([4, 2, 3], 4),  # Test 15
        ([100, 50, 25, 10], 100), # Test 16
        ([5, 4, 3, 2], 5), # Test 17
        ([6, 5, 4, 3, 2, 1], 6), # Test 18
        ([4, 2, 3], 4), # Test 19
        ([15, 14, 10, 8, 7, 9, 3, 2, 4], 15), # Test 20
    ]
    return cases


# tests.py

def test_is_full_binary_tree():
    # Sample TreeNode creation
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    # Test cases
    cases = [
        (node1, True),  # This is full
        (node2, True),  # This is a single node, also considered full
    ]
    return cases

def test_get_tree_height():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node4.right = node5  # This forms a tree of height 4

    return [
        (node1, 4),
        (node3, 1),
        (None, 0)
    ]