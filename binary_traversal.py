# Binary tree node
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Level Order Traversal (Breadth First)
def level_order(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Creating tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

print("\nLevel Order Traversal:")
level_order(root)


# Step 1: Start
# Step 2: If root is NULL, go to Step 8
# Step 3: Inorder Traversal
# Step 4: Traverse left → Visit root → Traverse right
# Step 5: Preorder Traversal
# Step 6: Visit root → Traverse left → Traverse right
# Step 7: Postorder Traversal
# Step 8: Traverse left → Traverse right → Visit root
# Step 9: Level Order Traversal
# Step 10: Insert root into queue and process level by level
# Step 11: Stop