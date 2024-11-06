steps = 0
def greatestNumber(array):
    global steps
    for i in range(len(array) - 1):
        print(f"We are now comparing {array[i]} and {array[i+1]}.")
        steps += 1
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    return array[len(array) - 1]

myArray = [4, 7, 500000, 17, 39, 99, 43, 324, 5476984, 435348795683456]

print(greatestNumber(myArray))
print(steps)
