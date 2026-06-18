## Author: Lane Dorscher
## Date: 05/08/2026

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_bst(root, key):
    """
    Insert a new TreeNode with the given key into the binary search tree rooted at 'root'.
    Return the root of the modified tree.
    """
    if root is None: 
        return TreeNode(key)
    elif key < root.val:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)

    return root

def find_max_heap(arr):
    """
    Given a max heap 'arr', return the maximum element (i.e., the root of the heap).
    If the heap is empty, return None.
    """
    if arr is None or len(arr) == 0: return None
    return arr[0]

def is_full_binary_tree(root: TreeNode):
    """
    Check if the binary tree rooted at 'root' is a full binary tree.
    Return True if it is, otherwise return False.
    """
    if not root: return True
    if not root.left and not root.right:
        return True
    if root.left and root.right:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    return False


def get_tree_height(root: TreeNode):
    """
    Return the height of the binary tree rooted at 'root'.
    """
    if not root:
        return 0
    left = get_tree_height(root.left)
    right = get_tree_height(root.right)

    max = left
    if right > left:
        max = right

    return max + 1 