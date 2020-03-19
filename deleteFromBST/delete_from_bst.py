class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def find_max(t):
    """
    Traverse a binary tree to find its max (far right)
    :param t: root of the tree
    :return: the max node
    """
    while t and t.right:
        t = t.right
    return t


def delete_bst_nodes(t, value):
    """
    Delete value node from  a binary tree and preserve BST property.
    - Traverse the tree to find the node to delete;
    - If found:
        1) Node has no children, just return None to the caller (which set
        its left/right node to the returned None)
        2) Node has one child, just return the child to the caller (which set
        its left/right node to the returned child and thus detach the node to delete)
        3) Node has both children:
           - Find the max in left subtree (min in right subtree would work too)
           - Make the value of the node to delete as the max just found
           - Remove the above duplicated node from the subtree
           - Return the root of the subtree, which now doesn't contain the deleted node
    :param t: Root of the tree
    :param value: The value to delete
    :return: Root of the tree, without the deleted node if found
    """
    if not t:
        return t

    # Value is in left subtree
    if t.value > value:
        t.left = delete_bst_nodes(t.left, value)
    # Value is in right subtree
    elif t.value < value:
        t.right = delete_bst_nodes(t.right, value)
    # Value is this node!
    else:
        # If no children, None will be returned to the caller
        # This means t.left or t.right of the caller will be set to None
        # And so this node is detached (removed)
        if not t.left and not t.right:
            return None
        # No left child, return right child
        # This means t.left or t.right of the caller will be set to right child
        # And so this node is detached (removed)
        elif not t.left:
            return t.right
        # No right child, return left child
        # This means t.left or t.right of the caller will be set to left child
        # And so this node is detached (removed)
        elif not t.right:
            return t.left
        # Both children exists
        else:
            # Find max of left node to keep BST property (min of right node would work too)
            max_of_left = find_max(t.left)
            # Clone the value into this node
            t.value = max_of_left.value
            # Set the left subtree of this cloned node with the current left subtree head
            # after removing the duplicated/cloned node from it
            t.left = delete_bst_nodes(t.left, max_of_left.value)

    return t


def deleteFromBST(t, queries):
    for value_to_rm in queries:
        t = delete_bst_nodes(t, value_to_rm)
    return t


root = Tree(5)
root.left = Tree(2)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right = Tree(6)
root.right.right = Tree(8)
root.right.right.left = Tree(7)

deleteFromBST(root, [4,5,6])
