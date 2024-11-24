# Eigen oplossing

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

def shortest_path(starting_vertex, final_vertex):
    cheapest_previous_stopover_vertex_table = {}
    
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

                cheapest_previous_stopover_vertex_table[adjacent_vertex.value] = current_vertex.value

                queue.enqueue(adjacent_vertex)

    shortest_path = []

    current_vertex_name = final_vertex.value
    while current_vertex_name != starting_vertex.value:
        shortest_path.append(current_vertex_name)
        current_vertex_name = cheapest_previous_stopover_vertex_table[current_vertex_name]
    
    shortest_path.append(starting_vertex.value)
    shortest_path.reverse()

    return shortest_path

idris = Vertex("idris")
kamil = Vertex("kamil")
talia = Vertex("talia")
lina = Vertex("lina")
ken = Vertex("ken")
marco = Vertex("marco")
sasha = Vertex("sasha")

idris.add_adjacent_vertex(kamil)
idris.add_adjacent_vertex(talia)

kamil.add_adjacent_vertex(idris)
kamil.add_adjacent_vertex(lina)

talia.add_adjacent_vertex(idris)
talia.add_adjacent_vertex(ken)

lina.add_adjacent_vertex(kamil)
lina.add_adjacent_vertex(sasha)

ken.add_adjacent_vertex(talia)
ken.add_adjacent_vertex(marco)

marco.add_adjacent_vertex(ken)
marco.add_adjacent_vertex(sasha)

sasha.add_adjacent_vertex(lina)
sasha.add_adjacent_vertex(marco)

print(shortest_path(idris, sasha))