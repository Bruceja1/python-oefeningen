basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"}
]

football_players = [
    {"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
    {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
    {"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
    {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]

def multiple_sports(array1, array2):
    # Add all names from both lists into one dictionary O(2N)
    # for each name: if name is already in dict; tally += 1
    # list.append firstname+lastname
    # return list

    name_collection = {}
    for player in basketball_players:
        name_collection[player["first_name"]] = 1

    print(name_collection)



print(basketball_players[0]["first_name"])
print(football_players[0]["first_name"])
multiple_sports(basketball_players, football_players)