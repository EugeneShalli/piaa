from random import randint
from typing import Optional
from src.BinTree import BinaryTree


class Cartesian(BinaryTree):
    class Node(BinaryTree.Node):
        __slots__ = ['x', 'left', 'right', 'parent', 'y']

        def __init__(self, x, parent=None, y=None):
            self.x = x
            self.parent = parent
            self.right = None
            self.left = None
            self.y = randint(0, 10000) if y is None else y

    @staticmethod
    def _merge(a, b) -> Optional[Node]:
        """

        :param a: корень дерева a
        :param b: корень дерева b
        :return: корень merged дерева c
        """
        if a is None:
            return b
        if b is None:
            return a

        if a.y > b.y:
            a.right = Cartesian._merge(a.right, b)
            return a
        else:
            b.left = Cartesian._merge(a, b.left)
            return b
        
        
    @staticmethod
    def _split(root: Node, key: int) -> tuple:
        """

        :param root: корень дерева для split
        :param key: ключ для split
        :return: пара корней после split по ключу
        """
        if root is None:
            return None, None
        if root.x < key:
            root.right, b = Cartesian._split(root.right, key)
            return root, b
        else:
            a, root.left = Cartesian._split(root.left, key)
            return a, root

    def __init__(self, x):
        self.head = Cartesian.Node(x)

    def insert(self, x):
        """
        Добавление вершины в дерево.
        """
        less, greater = Cartesian._split(self.head, x)
        self.head = Cartesian._merge(Cartesian._merge(less, Cartesian.Node(x, parent=None)), greater)

    def find_node(self, x):
        """
        Поиск вершины с заданным значением и восстановление ссылок на родителей
        """
        current_node = self.head
        while current_node is not None and current_node.x != x:
            if current_node.x > x:
                if current_node.left is not None:
                    current_node.left.parent = current_node
                current_node = current_node.left
            else:
                if current_node.right is not None:
                    current_node.right.parent = current_node
                current_node = current_node.right
        else:
            return current_node
