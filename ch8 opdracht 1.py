steps = 0
def intersection(array1, array2):
    global steps
    result = []
    hash1 = {}

    for number in array1:
        hash1[number] = True
        steps+=1
    print(hash1)

    for number in array2:
        if number in hash1:
            result.append(number)
            steps+=1
        steps+=1

    return result

myArray1 = [1, 2, 3, 4, 5]
myArray2 = [0, 2, 4, 6, 8]

print(intersection(myArray1, myArray2))
print(steps)
        
