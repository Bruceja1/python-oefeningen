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

    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = self.first_node.next_node
        return removed_node

class Queue:
    def __init__(self, queue = None):
        self.queue = DoublyLinkedList()

    def enqueue(self, element):
        self.queue.insert_at_end(element)

    def dequeue(self):
        removed_node = self.queue.remove_from_front()
        return removed_node.data

    def read(self):
        if self.queue.first_node == None:
            return None

        return self.queue.first_node.data

myQueue = Queue()
myQueue.enqueue("Apple")
#print(myQueue.read())
print(myQueue.dequeue())

    
        
