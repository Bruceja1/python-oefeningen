def BinarySearch(array, searchValue):
    index = len(array) // 2
    while True:  
        print(f"Dit is de huidige index: {index}")
        if searchValue == array[index]:
            print(f"De zoekterm {searchValue} is gevonden op index {index}!")
            return index
        if index == len(array) - 1 or index == 0:
            break
        elif searchValue < array[index]:
            index = index // 2
            print(f"De zoekterm is kleiner dan de index. De nieuwe index wordt: {index}")
        elif searchValue > array[index]:
            index = (len(array) - index) // 2 + index
            print(f"De zoekterm is kleiner dan de index. De nieuwe index wordt: {index}")
        
    print("Zoekterm niet gevonden.")

myArray = [23, 25, 37, 56, 90, 95, 97, 103, 107, 109, 114, 117, 119]
mySearchValue = 113
BinarySearch(myArray, mySearchValue)
