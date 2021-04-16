class BinaryTree:
    class Node:
        __slots__ = ['x', 'left', 'right', 'parent']

        def __init__(self, x, parent=None):
            self.x = x
            self.parent = parent
            self.right = None
            self.left = None

        def __str__(self):
            return str(self.x)

        def insert(self, x):
            if self.x < x:
                if self.right is None:
                    self.right = BinaryTree.Node(x, self)
                else:
                    self.right.insert(x)
            else:
                if self.left is None:
                    self.left = BinaryTree.Node(x, self)
                else:
                    self.left.insert(x)

    def __init__(self, x):
        self.head = BinaryTree.Node(x)

    def insert(self, x):
        """
        Добавление вершины в дерево.
        """
        self.head.insert(x)

    def find_node(self, x):
        """
        Поиск узла с заданным значением.
        """
        current_node = self.head
        while current_node is not None and current_node.x != x:
            if current_node.x > x:
                current_node = current_node.left
            else:
                current_node = current_node.right
        else:
            return current_node

    def text_find_node(self, x):
        return '+' if self.find_node(x) is not None else '-'

    def find_next_node(self, x):
        """
        Поиск следующего по значению узла дерева.
        """
        current_node = self.find_node(x)
        if current_node.right is None:
            try:
                while current_node.parent.x < x:
                    current_node = current_node.parent
                else:
                    return current_node.parent
            except AttributeError:
                return None

        else:
            current_node = current_node.right
            while current_node.left is not None:
                current_node = current_node.left
            return current_node

    def text_find_next_node(self, x):
        result = self.find_next_node(x)
        return result if result is not None else '-'
