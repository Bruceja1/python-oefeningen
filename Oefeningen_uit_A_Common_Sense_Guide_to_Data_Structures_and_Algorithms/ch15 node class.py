class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.leftChild = left
        self.rightChild = right

def search(searchValue, node):
    if node == None or node.value == searchValue:
        return node

    elif searchValue < node.value:
        return search(searchValue, node.leftChild)

    else:
        return search(searchValue, node.rightChild)

def insert(value, node):
    if value < node.value:
        if node.leftChild == None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)

    elif value > node.value:
        if node.rightChild == None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)

def delete(value, node):
    if node.value < value && node.rightChild != None:
        delete(value, node.rightChild)
    elif node.value > value && node.leftChild != None:
        delete(value, node.leftChild)

    if node.value != value && node.leftChild == None && node.rightChild == None:
        return "Value not found!"

    if node.value == value:
        
        

node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)

print(search(25, root))
