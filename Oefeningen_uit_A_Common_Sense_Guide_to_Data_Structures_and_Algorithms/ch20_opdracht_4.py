# Eigen oplossing
def find_greatest_product(array):
    highest_number = array[0]
    second_highest_number = array[0]

    for i in range(0, len(array)):
        array[i] = abs(array[i])
        if array[i] > highest_number:
            highest_number = array[i]

        elif array[i] > second_highest_number:
            second_highest_number = array[i]

    return highest_number * second_highest_number

# Oplossing boek
def greatest_product(array):
    greatest_number = -999999
    second_to_greatest_number = -999999

    lowest_number = 999999
    second_to_lowest_number = 999999

    for number in array:
        if number >= greatest_number:
            second_to_greatest_number = greatest_number
            greatest_number = number
        
        elif number > second_to_greatest_number:
            second_to_greatest_number = number

        if number <= lowest_number:
            second_to_lowest_number = lowest_number
            lowest_number = number
        
        elif number > lowest_number and number < second_to_lowest_number:
            second_to_lowest_number = number
        
    greatest_product_from_two_highest = greatest_number * second_to_greatest_number
    greatest_product_from_two_lowest = lowest_number * second_to_lowest_number

    if greatest_product_from_two_highest > greatest_product_from_two_lowest:
        return greatest_product_from_two_highest
    
    else:
        return greatest_product_from_two_lowest

myArray = [5, -10, -6, 9, 4]
#print(find_greatest_product(myArray))
print(greatest_product(myArray))