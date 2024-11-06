def triangle(number):
    if number == 1:
        return 1
    
    return number + triangle(number - 1)

print(triangle(6))
