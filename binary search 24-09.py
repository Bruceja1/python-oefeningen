myArray = [1,2,3,4,5]

def binary_search(array, search_value):
    upper_bound = len(array) - 1
    lower_bound = 0

    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2

        if array[midpoint] == search_value:
            return midpoint

        elif search_value < array[midpoint]:
            upper_bound = midpoint - 1

        elif search_value > array[midpoint]:
            lower_bound = midpoint + 1

    return None

print(binary_search(myArray, 5))

if "hi" < "test":
    print(True)

else:
    print(False)
