steps = 0
def selection_sort(array):
    global steps
    low = 0
    start_index = 0
    
    while start_index < len(array) - 1:
        low = start_index
        print(f"The value for low is now {low}")
        for i in range(start_index, len(array)):
            print(f"Comparing {array[i]} and {array[low]}")
            if array[i] < array[low]:
                low = i
            steps += 1
        print(f"The array was {array}")
        array[start_index], array[low] = array[low], array[start_index]
        start_index += 1
        steps += 1
        print(f"The array is now {array} and the new starting index is {start_index}")        
    return array

def selection_sort2(array):
    for i in range(len(array) - 1):
        low = i
        for j in range(i+1, len(array)):
            if (array[j] < array[low]):
                low = j 

        if (low != i):
            temp = array[i]
            array[i] = array[low]
            array[low] = temp

    return array

myArray = [76, 4, 43, 54, 3, 23, 92]
print(selection_sort2(myArray))
# print(steps)

