# Eigen oplossing

def find_missing_integer(array):
    integer_dict = {}
    highest_number = -999999

    for i in range(0, len(array)):
        if array[i] > highest_number:
            highest_number = array[i]
        integer_dict[array[i]] = True
    
    if 0 not in integer_dict:
            return f"\nThe missing integer is {0}!\n"
    
    else:
        for i in range(0, len(array)):
             if array[i] != highest_number:
                  if array[i] + 1 not in integer_dict:
                       return f"\nThe missing integer is {array[i] + 1}!\n"

myArray = [8, 2, 3, 9, 4, 7, 5, 0, 6]
print(find_missing_integer(myArray))