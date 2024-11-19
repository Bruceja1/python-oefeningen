def countdown(number):
    if number == 0:
        print(number)
    else:
        print(number)
        number -= 1
        countdown(number)

countdown(10)
