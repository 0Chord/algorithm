class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def tree_insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key)
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.key)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key)


def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent
    return y


bst = BinarySearchTree()
nodes = [Node(i) for i in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]]
for node in nodes:
    bst.tree_insert(node)

preorder_traversal(bst.root)
inorder_traversal(bst.root)
postorder_traversal(bst.root)

bst.tree_delete(bst.root.left.right.right.left)
preorder_traversal(bst.root)

print(tree_search(bst.root, 13).key)
print(iterative_tree_search(bst.root, 13).key)

print(tree_minimum(bst.root).key)
print(tree_maximum(bst.root).key)

print(tree_successor(bst.root.left.right).key)
