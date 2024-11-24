#array = [3,5,6,234213,765,23213]
#array = [234, 34535, 178, 3, 5435344, 454, 98, 565]
array = [1,4,8,5,2]

def partition(left_pointer, right_pointer):
    #global array
    pivot_index = right_pointer
    pivot = array[right_pointer]
    right_pointer -= 1

    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1

        while array[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            break

        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

        left_pointer += 1

    array[left_pointer], array[pivot_index] = array[pivot_index], array[left_pointer]
    print(array)
    return left_pointer

def quick_select(left_index, right_index, n_biggest):
    pivot_index = partition(left_index, right_index)
    print(f"This is the value of n_biggest: {n_biggest}")
    print(f"This is the value of pivot_index: {pivot_index}")
    
    if pivot_index == n_biggest:
        return array[n_biggest]

    if pivot_index > n_biggest:
            return quick_select(left_index, pivot_index - 1, n_biggest)

    elif pivot_index < n_biggest:
            return quick_select(pivot_index + 1, right_index, n_biggest)

def select_n_biggest():
    valid = {}
    for i in range(1, len(array) + 1):
        valid[i] = True
    print(valid)


    while True:
        n = input(f"Please select a number from 1 to {len(array)}: \n")

        try:
            n = int(n)
            if n not in valid:
                print("Value is out of range.")
            else:
                break
        except:
            print("Invalid input.")
     
    print(quick_select(0, len(array) - 1, n-1))

select_n_biggest()

    
