class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)

def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)

def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]

def build_tree_pre_in(preorder_list, inorder_list):
    if not preorder_list or not inorder_list:
        return None
    root_val = preorder_list[0]
    root = Node(root_val)
    idx = inorder_list.index(root_val)
    root.left = build_tree_pre_in(preorder_list[1:1+idx], inorder_list[:idx])
    root.right = build_tree_pre_in(preorder_list[1+idx:], inorder_list[idx+1:])
    return root

def build_tree_post_in(postorder_list, inorder_list):
    if not postorder_list or not inorder_list:
        return None
    root_val = postorder_list[-1]
    root = Node(root_val)
    idx = inorder_list.index(root_val)
    root.left = build_tree_post_in(postorder_list[:idx], inorder_list[:idx])
    root.right = build_tree_post_in(postorder_list[idx:-1], inorder_list[idx+1:])
    return root

# Example traversal tree
example_tree = Node(8)
example_tree.left = Node(3)
example_tree.right = Node(10)
example_tree.left.left = Node(1)
example_tree.left.right = Node(6)
example_tree.left.right.left = Node(4)
example_tree.left.right.right = Node(7)
example_tree.right.right = Node(14)
example_tree.right.right.left = Node(13)

print("Preorder:", preorder(example_tree))
print("Inorder:", inorder(example_tree))
print("Postorder:", postorder(example_tree))

# Reconstruction examples
pre = ['Q','W','E','R','T','Y','U','I']
ino = ['E','W','T','R','Q','Y','U','I']
tree1 = build_tree_pre_in(pre, ino)
print("Reconstructed Pre+Inorder Tree, Inorder Traversal:", inorder(tree1))

post = ['J','I','L','M','N','K','H']
ino2 = ['J','I','H','L','K','M','N']
tree2 = build_tree_post_in(post, ino2)
print("Reconstructed Post+Inorder Tree, Inorder Traversal:", inorder(tree2))
