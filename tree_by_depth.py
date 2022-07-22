from tree import Tree
from tree import Node


def height(node, h=0):
    leftHeight = height(node.left, h + 1) if node.left else h
    rightHeight = height(node.right, h + 1) if node.right else h
    return max(leftHeight, rightHeight)


def __getNodesAtDepth(node, depth, nodes):
    if depth == 0:
        nodes.append(node)
        return nodes
    if node.left:
        __getNodesAtDepth(node.left, depth - 1, nodes)
    else:
        nodes.extend([None] * 2 ** (depth - 1))
    if node.right:
        __getNodesAtDepth(node.right, depth - 1, nodes)
    else:
        nodes.extend([None] * 2 ** (depth - 1))
    return nodes


def getNodesAtDepth(node, depth):
    return __getNodesAtDepth(node, depth, [])


def node_array_to_str(nodeArray):
    str_list = [str(node.data if node else None) for node in nodeArray]
    # create a row with values separated by commas
    return ", ".join(str_list)


# build sample tree
tree = Tree(Node(50), "Tree nodes at individual depths")
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)

# print the tree as a visual cue
tree.print()

tree_heigth = height(tree.root)

for i in range(0, tree_heigth + 1):
    print("Nodes at depth [{}]: {}".format(
        i, node_array_to_str(getNodesAtDepth(tree.root, i))))
