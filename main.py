from binary_expression_tree import BinaryExpressionTree

expressions = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -"
]

print("----- Binary Expression Tree -----")
for exp in expressions:
    tree = BinaryExpressionTree()
    tree.build_tree(exp)
    print(f"Infix Expression: {tree.inorder()}")
    print(f"Postfix Expression: {tree.postorder()}")
    print(f"Evaluated Result: {tree.evaluate_tree()}\n")
