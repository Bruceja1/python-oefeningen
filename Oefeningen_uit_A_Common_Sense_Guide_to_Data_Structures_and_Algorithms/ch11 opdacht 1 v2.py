def character_count(array):
    if len(array) == 1:
        return len(array[0])
    return len(array[0]) + character_count(array[1:])

myArray = ["ab", "c", "def", "ghij"]
print(character_count(myArray))
