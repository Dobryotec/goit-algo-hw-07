class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_sum(node):
    if node is None:
        return 0
    return node.val + find_sum(node.left) + find_sum(node.right)

   
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 6)
root = insert(root, 8)

print (f"Total sum = {find_sum(root)}")