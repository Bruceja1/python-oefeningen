class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        #print(visited_vertices)
        #print(f"The adjacent vertex of {vertex.value} is: {adjacent_vertex.value}")
        if adjacent_vertex.value not in visited_vertices:          
            dfs_traverse(adjacent_vertex, visited_vertices)

alice = Vertex("alice")
bob = Vertex("bob")
fred = Vertex("fred")
helen = Vertex("helen")
candy = Vertex("candy")
derek = Vertex("derek")
elaine = Vertex("elaine")
gina = Vertex("gina")
irena = Vertex("irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)

bob.add_adjacent_vertex(fred)
bob.add_adjacent_vertex(alice)

fred.add_adjacent_vertex(bob)
fred.add_adjacent_vertex(helen)

helen.add_adjacent_vertex(candy)
helen.add_adjacent_vertex(fred)

candy.add_adjacent_vertex(helen)
candy.add_adjacent_vertex(alice)

derek.add_adjacent_vertex(alice)
derek.add_adjacent_vertex(elaine)
derek.add_adjacent_vertex(gina)

elaine.add_adjacent_vertex(alice)
elaine.add_adjacent_vertex(derek)

gina.add_adjacent_vertex(derek)
gina.add_adjacent_vertex(irena)

irena.add_adjacent_vertex(gina)

for friend in alice.adjacent_vertices:
    print("1")

for friend in candy.adjacent_vertices:
    print("2")

dfs_traverse(alice)
