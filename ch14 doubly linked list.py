class Node:
    def __init__(self, data, next_node = None, previous_node = None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

class DoublyLinkedList:
    def __init__(self, first_node = None, last_node = None):
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.first_node == None:
            self.first_node = new_node
            self.last_node = new_node

        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node


node_1 = Node("Bob")
node_2 = Node("Jill")
node_3 = Node("Emily")
node_4 = Node("Greg")
node_5 = Node("Sue")

node_1.next_node = node_2

node_2.next_node = node_3
node_2.previous_node = node_1

node_3.next_node = node_4
node_3.previous_node = node_2

node_4.next_node = node_5
node_4.previous_node = node_3


list = DoublyLinkedList()
list.insert_at_end("Jerry")
print(list.last_node.data)
