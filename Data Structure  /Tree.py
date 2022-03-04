class Node:
    def __init__(self, number):
        self.childleft = None
        self.childright = None
        self.nodedata = number

root = Node(8)
root.childleft = Node(3)
root.childright = Node(10)
root.childleft.childleft = Node(1)
root.childleft.childright = Node(6)
root.childleft.childright.childright = Node(7)
root.childleft.childright.childleft = Node(4)
root.childright.childright = Node(14)
root.childright.childright.childleft = Node(13)
print(root.nodedata)
