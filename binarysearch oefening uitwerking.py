# Python uitwerking van Ruby voorbeeld uit het boek
def binary_search(array, search_value):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        if array[midpoint] == search_value:
            print("Gevonden!")
            return midpoint
        elif array[midpoint] > search_value:
            upper_bound = midpoint - 1
        elif array[midpoint] < search_value:
            lower_bound = midpoint + 1
    print("Niet gevonden!")
    return None

myArray = [3, 7 ,9, 12, 13, 15, 19, 25, 36, 48]
mySearchValue = 13

binary_search(myArray, mySearchValue)
