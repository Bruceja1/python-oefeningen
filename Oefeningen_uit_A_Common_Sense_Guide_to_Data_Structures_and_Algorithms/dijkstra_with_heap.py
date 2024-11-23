cheapest_prices_table = {}

class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price

class Heap:
    global cheapest_prices_table

    def __init__(self):
        self.data = []

    def root_node(self):
        if len(self.data) == 0:
            return None
            
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index):
        return (index * 2) + 1

    def right_child_index(self, index):
        return (index * 2) + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.data.append(value)

        new_node_index = len(self.data) - 1

        # Cheapest city in front of the queue. Cheapest means the city with lowest price 
        # in the cheapest_prices_table
        new_node_name = self.data[new_node_index].name
        new_node_parent_name = self.data[self.parent_index(new_node_index)].name

        while new_node_index > 0 and cheapest_prices_table[new_node_name] < cheapest_prices_table[new_node_parent_name]:
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            new_node_index = self.parent_index(new_node_index)

    def has_smaller_child(self, index):
        left_child_exists = True
        if self.left_child_index(index) >= len(self.data) or self.data[self.left_child_index(index)] == None:
            left_child_exists = False
        
        right_child_exists = True
        if self.right_child_index(index) >= len(self.data) or self.data[self.right_child_index(index)] == None:
            right_child_exists = False

        if left_child_exists and cheapest_prices_table[self.data[self.left_child_index(index)].name] < cheapest_prices_table[self.data[index].name] or right_child_exists and cheapest_prices_table[self.data[self.right_child_index(index)].name] < cheapest_prices_table[self.data[index].name]:
            return True

    def calculate_smaller_child_index(self, index):
        if not self.data[self.right_child_index(index)]:
            return self.left_child_index(index)
        
        if cheapest_prices_table[self.data[self.right_child_index(index)].name] < cheapest_prices_table[self.data[self.left_child_index(index)].name]:
            return self.right_child_index(index)
        
        else:
            return self.left_child_index(index)

    def delete(self):               
        self.data[0] = self.data[-1]
        self.data.pop()

        trickle_node_index = 0

        while self.has_smaller_child(trickle_node_index):
            smaller_child_index = self.calculate_smaller_child_index(trickle_node_index)

            self.data[trickle_node_index], self.data[smaller_child_index] = self.data[smaller_child_index], self.data[trickle_node_index]
            print(self.data)
            trickle_node_index = smaller_child_index

def dijkstra_shortest_path(starting_city, final_destination):
    global cheapest_prices_table
    cheapest_previous_stopover_city_table = {}

    unvisited_cities = Heap()

    # Could also be an array, but hash is faster cus we do lookups
    visited_cities = {}

    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city

    while current_city:
        visited_cities[current_city.name] = True

        print(f"The length of the heap is {len(unvisited_cities.data)}")
        if len(unvisited_cities.data) > 0:
            print(f"Let's delete this node from the unvisited cities list: {unvisited_cities.data}")
            unvisited_cities.delete()
     
        for adjacent_city, price in current_city.routes.items():
            price_through_current_city = cheapest_prices_table[current_city.name] + price

            if adjacent_city.name not in cheapest_prices_table or price_through_current_city < cheapest_prices_table[adjacent_city.name]:
                cheapest_prices_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name

            if adjacent_city.name not in visited_cities:
                unvisited_cities.insert(adjacent_city)
        
        current_city = unvisited_cities.root_node()

    shortest_path = []

    current_city_name = final_destination.name
    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]

    shortest_path.append(starting_city.name)
    shortest_path.reverse()
    return shortest_path


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

print(dijkstra_shortest_path(atlanta, el_paso))

