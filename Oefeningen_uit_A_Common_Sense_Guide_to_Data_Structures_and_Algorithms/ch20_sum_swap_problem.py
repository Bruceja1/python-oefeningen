def sum_swap(array1, array2):
    for i in range(0, len(array1)):
        for j in range(0, len(array2)):
            sum_of_array1 = sum(array1) - array1[i] + array2[j]
            sum_of_array2 = sum(array2) - array2[j] + array1[i]

            if sum_of_array1 == sum_of_array2:
                return [i, j]
    
    return None

myArray1 = [5,3,2,9,1]
myArray2 = [1,12,5]
print(sum_swap(myArray1, myArray2))