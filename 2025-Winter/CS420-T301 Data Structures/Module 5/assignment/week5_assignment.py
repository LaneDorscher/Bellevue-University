class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_into_bst(root, value):
    """
    Inserts a value into a Binary Search Tree and returns the root of the tree.
    """

    if (root is None):
        return TreeNode(value)

    if (value < root.value):
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)

    return root

def is_valid_bst(root, lower_bound=float('-inf'), upper_bound=float('inf')):
    """
    Determines if a binary tree is a valid Binary Search Tree.
    """

    if (root is None):
        return True

    if not (root.value > lower_bound and root.value < upper_bound):
        return False
    
    return is_valid_bst(root.left, lower_bound, root.value) and is_valid_bst(root.right, root.value, upper_bound)

def inorder_traversal(root):
    """
    Performs in-order traversal on a binary tree and returns a list of values.
    """
    if (root is None):
        return []
    
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)
