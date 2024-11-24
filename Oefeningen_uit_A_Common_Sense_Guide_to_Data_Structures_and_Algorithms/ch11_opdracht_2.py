# eigen oplossing
result = []
def even_numbers(numberList):
    global result

    if len(numberList) == 1:
        if numberList[0] % 2 == 0:
            result.append(numberList[0])
        return

    if numberList[0] % 2 == 0:
        result.append(numberList[0])

    even_numbers(numberList[1:])

    return result

myList = [1,2,3,4,5,6,7,8,9,10]
#print(even_numbers(myList))

# oplossing boek
def select_even(array):
    if len(array) == 0:
        return []

    if array[0] % 2 == 0:
        return [array[0]] + select_even(array[1:])
    else:
        return select_even(array[1:])
    
print(select_even(myList))
