myArray = [2,1,0,6,7]

def missing_number(array):
    array.sort()
    for i in range(0, len(array)):
        if array[i] != i:
            return i
        
print(missing_number(myArray))
