class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        current_node = self.first_node

        for i in range(0, index + 1):     
            if i == index:
                return current_node.data

            if current_node.next_node == None:
                return "Nope"
            
            current_node = current_node.next_node

    def index_of(self, value):
        current_node = self.first_node
        current_index = 0

        while current_node != None:
            if current_node.data == value:
                return current_index

            current_node = current_node.next_node
            current_index += 1

        return None

    def insert_at_index(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next_node = first_node
            self.first_node = new_node
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        if index == 0:
            self.first_node = first_node.next_node
            return

        current_node = self.first_node
        current_index = 0

        while current_index < (index - 1):
            current_node = current_node.next_node
            current_index += 1

        node_after_deleted_node = current_node.next_node.next_node
        current_node.next_node = node_after_deleted_node

    # eigen oplossing
    def reverse_order(self):
        current_node = self.first_node
        one_node_ahead = current_node.next_node
        two_nodes_ahead = one_node_ahead.next_node
        
        while current_node:
            one_node_ahead.next_node = current_node
            current_node = one_node_ahead
            one_node_ahead = two_nodes_ahead
            if one_node_ahead == None:
                self.first_node = current_node
                break
            two_nodes_ahead = one_node_ahead.next_node
        return
    
    '''
    # oplossing boek  
    def reverse_order(self):
        previous_node = None
        current_node = self.first_node

        while current_node:
            next_node = current_node.next_node

            current_node.next_node = previous_node

            previous_node = current_node
            current_node = next_node

        self.first_node = previous_node
     '''       
class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4
    
list = LinkedList(node_1)
print(list.read(0))
print(list.read(1))
print(list.read(2))
print(list.read(3))

list.reverse_order()
print(list.read(0))
print(list.read(1))
print(list.read(2))
print(list.read(3))
