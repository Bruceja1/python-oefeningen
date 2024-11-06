#array = [5,6,2,4,8]
#array = [0,5,2,1,6,3,4,7]
#array = [3,2,7,12,3,5]
array = [234, 34535, 178, 3, 5435344, 454, 98, 565]
steps = 0

def partition(left_pointer, right_pointer):
    global array
    global steps
    #print("Initial Array:", array)
     
    pivot_index = right_pointer
    pivot = array[pivot_index]
    right_pointer -= 1
    #print("Pivot Index:", pivot_index)
    #print("Pivot Value:", pivot)
    #print("Left Pointer at start:", left_pointer)
    #print("Right Pointer at start:", right_pointer)

   
    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1

            steps+=1

        while array[right_pointer] > pivot:
            right_pointer -= 1

            steps+=1
            
        if left_pointer >= right_pointer:
            #print(f"Swapping pivot {array[pivot_index]} with {array[left_pointer]}")
            temp = array[left_pointer]
            array[left_pointer] = array[pivot_index]
            array[pivot_index] = temp
            #array[left_pointer], array[pivot_index] = array[pivot_index], array[left_pointer]
            steps+=1

            break

        else:
            #print(f"Swapping {array[left_pointer]} with {array[right_pointer]}")
            #array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            temp = array[left_pointer]
            array[left_pointer] = array[right_pointer]
            array[right_pointer] = temp
            steps+=1

        #print("Array after swap:", array)
        left_pointer += 1
        steps+=1
    #print("Final Partitioned Array:", array)
    return left_pointer

def quick_sort(left_index, right_index):
    global steps
    
    if right_index - left_index <= 1:
        return

    pivot_index = partition(left_index, right_index)
    steps+=1

    quick_sort(left_index, pivot_index - 1)
    steps+=1
    quick_sort(pivot_index + 1, right_index)
    steps+=1

    return array

print(quick_sort(0, len(array) - 1))
print(steps)

