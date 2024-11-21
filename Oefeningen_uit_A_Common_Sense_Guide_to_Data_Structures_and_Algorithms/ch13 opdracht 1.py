myArray = [2,3,5,4]

def greatest_product(array):
    if len(array) < 3:
        return None
    
    array.sort()

    print(f"The greatest product is: {array[-1]} * {array[-2]} * {array[-3]}") 
    return array[-1] * array[-2] * array[-3]


print(greatest_product(myArray))
