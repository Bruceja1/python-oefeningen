class Vertex:
    def __init__(self, value, adjacent_vertices=[]):
        self.value = value
        self.adjacent_vertices = adjacent_vertices

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

alice = Vertex("alice")
bob = Vertex("bob")
cynthia = Vertex("cynthia")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)
cynthia.add_adjacent_vertex(bob)

friends = cynthia.adjacent_vertices()

for friend in friends:
    print(friend)

