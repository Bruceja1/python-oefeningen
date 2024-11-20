class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price

def dijkstra_shortest_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}

    unvisited_cities = []

    # Could also be an array, but hash is faster cus we do lookups
    visited_cities = {}

    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city

    while current_city:
        visited_cities[current_city.name] = True
        unvisited_cities.remove(current_city)

        for adjacent_city, price in current_city.routes:
            if adjacent_city.name not in visited_cities:
                unvisited_cities.append(adjacent_city)

            price_through_current_city = cheapest_prices_table[current_city.name] + price

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

for city in atlanta.routes:
    print(city.name)
    print(atlanta.routes[city])

