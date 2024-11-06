# Insertion sort reveals power of analyzing scenarios beyond the worst case.

# loop from 1 to end of array
# remove value at index i and store in temp variable
# compare value to the left to temp value
# if value is bigger, shift value to index i
# then look at the next left value
# else this is the end of the iteration. Insert temp value at the gap

def insertion_sort(array):
    for index in range(1, len(array)):
        
        temp_value = array[index]
        position = index - 1
        
        while position >= 0:
            if array[position] > temp_value:
                print(array)
                array[position + 1] = array[position]
                print(array)
                position = position - 1
            else:
                break
            
        array[position + 1] = temp_value
        
    return array

myArray = [23, 54, 1, 24, 234, 99]
print(insertion_sort(myArray))

                
           
              
              
