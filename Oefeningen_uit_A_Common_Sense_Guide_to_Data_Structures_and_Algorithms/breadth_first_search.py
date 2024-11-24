class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

class Queue:
    def __init__(self):
        self.data =[]

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        return self.data.pop(0)
    
    def read(self):
        if len(self.data) <= 0:
            return None
        
        return self.data[0]

def bfs_traverse(starting_vertex):
    queue = Queue()

    visited_vertices = {}
    visited_vertices[starting_vertex.value] = True
    queue.enqueue(starting_vertex)

    while queue.read():
        current_vertex = queue.dequeue()
        print(current_vertex.value)

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True

                queue.enqueue(adjacent_vertex)

alice = Vertex("alice")
bob = Vertex("bob")
candy = Vertex("candy")
derek = Vertex("derek")
elaine = Vertex("elaine")
fred = Vertex("fred")
gina = Vertex("gina")
helen = Vertex("helen")
irena = Vertex("irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)

bob.add_adjacent_vertex(alice)
bob.add_adjacent_vertex(fred)

candy.add_adjacent_vertex(alice)
candy.add_adjacent_vertex(helen)

derek.add_adjacent_vertex(alice)
derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)

elaine.add_adjacent_vertex(alice)
elaine.add_adjacent_vertex(derek)

fred.add_adjacent_vertex(bob)
fred.add_adjacent_vertex(helen)

gina.add_adjacent_vertex(derek)
gina.add_adjacent_vertex(irena)

helen.add_adjacent_vertex(fred)
helen.add_adjacent_vertex(candy)

irena.add_adjacent_vertex(gina)

bfs_traverse(alice)