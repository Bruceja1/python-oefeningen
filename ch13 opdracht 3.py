#variable
#sorting
#double loop

myArray = [2,5,1,2,4]

# O(N^2)
def greatest_number(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):     
            if array[i] < array[j]:
                break
            
            elif j == len(array) - 1:
                return array[i]

#print(greatest_number(myArray))

# O(N logN)
def greatest_number2(array):
    array.sort()

    return array[-1]

#print(greatest_number2(myArray))

# O(N)
def greatest_number3(array):
    biggest = 0
    for i in range(0, len(array)):
        if array[i] > biggest:
            biggest = array[i]

    return biggest

print(greatest_number3(myArray))

        
        
        
