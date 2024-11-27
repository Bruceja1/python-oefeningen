# Eigen oplossing

def reverse(array):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        array[left_index], array[right_index] = array[right_index], array[left_index]
        
        left_index += 1
        right_index -= 1
    
    return array

myArray = [1,2,3,4]
print(reverse(myArray))