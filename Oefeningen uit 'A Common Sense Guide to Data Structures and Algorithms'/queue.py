class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        self.data.pop(0)

    def read(self):
        return self.data[0]

x = Queue()

x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)

print(x.data)

x.dequeue()

print(x.data)

print(x.read())
