#array
#left pointer, right pointer
#left pointer = array[0]
#right pointer = array[-2]
#pivot = array[-1]

#array = [8,7,6,5,2]
array = [0,5,2,1,6,3,4,7]
steps = 0
def partition(left_pointer, right_pointer):
    global array
    global steps
    
    pivot_index = right_pointer
    right_pointer -= 1
    pivot = array[pivot_index]

    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1
                  
        while array[right_pointer] > pivot:
            right_pointer -= 1
            
        if left_pointer >= right_pointer:
            array[left_pointer], array[pivot_index] = array[pivot_index], array[left_pointer]
            steps+=1
            print(array)
            break

        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            steps+=1
    
    return left_pointer

def quick_sort(left_index, right_index):
    global array
    global steps
    
    if right_index - left_index <= 0:
        return

    pivot_index = partition(left_index, right_index)
    steps+=1
    
    quick_sort(left_index, pivot_index - 1)
    steps+=1
    quick_sort(pivot_index + 1, right_index)
    steps+=1

    return array

print(quick_sort(0, len(array)-1))
print(steps)
