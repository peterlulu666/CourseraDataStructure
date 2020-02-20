class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversal:
    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        print(node.data)
        self.in_order_traversal(node.right)

    def pre_order_traversal(self, node):
        if node is None:
            return
        print(node.data)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node is None:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.data)

    def insert_node(self, data):
        new_node = Node(data)
        return new_node


def main():
    traversal = Traversal()
    root = traversal.insert_node("Les")
    root.left = traversal.insert_node("Cathy")
    root.left.left = traversal.insert_node("Alex")
    root.left.right = traversal.insert_node("Frank")
    root.right = traversal.insert_node("Sam")
    root.right.left = traversal.insert_node("Nancy")
    root.right.right = traversal.insert_node("Violet")
    root.right.right.left = traversal.insert_node("Tony")
    root.right.right.right = traversal.insert_node("Wendy")

    traversal.in_order_traversal(root)
    traversal.pre_order_traversal(root)
    traversal.post_order_traversal(root)


main()
