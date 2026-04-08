from stack import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, postfix):
        s = Stack()
        for token in postfix.split():
            if token.isdigit():
                s.push(Node(token))
            elif token in "+-*/":
                node = Node(token)
                if s.is_empty():
                    raise ValueError("Stack empty, missing operand")
                node.right = s.pop()
                if s.is_empty():
                    raise ValueError("Stack empty, missing operand")
                node.left = s.pop()
                s.push(node)
            else:
                raise ValueError(f"Unsupported token: {token}")
        if s.is_empty():
            raise ValueError("No expression")
        self.root = s.pop()
        if not s.is_empty():
            raise ValueError("Unused tokens left in stack")

    def evaluate_tree(self, node=None):
        if node is None:
            node = self.root
        if node.left is None and node.right is None:
            return float(node.value)
        x = self.evaluate_tree(node.left)
        y = self.evaluate_tree(node.right)
        if node.value == '+':
            return x + y
        elif node.value == '-':
            return x - y
        elif node.value == '*':
            return x * y
        elif node.value == '/':
            return x / y

    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left is None and node.right is None:
            return node.value
        return f"({self.inorder(node.left)} {node.value} {self.inorder(node.right)})"

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node.left is None and node.right is None:
            return node.value
        return f"{self.postorder(node.left)} {self.postorder(node.right)} {node.value}"

post = ['J','I','L','M','N','K','H']
ino2 = ['J','I','H','L','K','M','N']
tree2 = build_tree_post_in(post, ino2)
print("Reconstructed Post+Inorder Tree, Inorder Traversal:", inorder(tree2))
