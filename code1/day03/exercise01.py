"""
    二叉树的使用
"""
from day02.squeue import SQueue


class LinkNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Binarytree:
    def __init__(self):
        self.root = None

    def create_tree(self, root=None, val_list=[]):
        if len(val_list) <= 0:
            return root
        if val_list[0] != '#':
            root = LinkNode(val_list[0])
            val_list.pop(0)
            root.left = self.create_tree(root, val_list)
            root.right = self.create_tree(root, val_list)
            return root
        else:
            root = None
            val_list.pop(0)
            return root

    def preorder(self, node):
        """
        先序循环打印
        :param node: 需要循环二叉树的根节点
        :return:
        """
        if node is None:
            return
        print(node.value, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """
        中序循环打印
        :param node: 需要循环二叉树的根节点
        :return:
        """
        if node is None:
            return
        self.inorder(node.left)
        print(node.value, end=' ')
        self.inorder(node.right)

    def postorder(self, node):
        """
        中序循环打印
        :param node: 需要循环二叉树的根节点
        :return:
        """
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=' ')

    def levelorder(self, node):
        """
            层级遍历打印
        :param node: 需要循环二叉树的根节点
        :return:
        """
        queue = SQueue()
        queue.join_queue(node)
        while not queue.is_empty():
            node = queue.out_queue()
            if node.left:
                queue.join_queue(node.left)
            if node.right:
                queue.join_queue(node.right)
            print(node.value, end=' ')


if __name__ == '__main__':
    bt = Binarytree()
    node1 = bt.create_tree(None, list('ABC##D##EF##HI####'))
    bt.preorder(node1)
    print()
    bt.inorder(node1)
    print()
    bt.postorder(node1)
    print()
    bt.levelorder(node1)
