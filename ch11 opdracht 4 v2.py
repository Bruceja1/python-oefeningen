def index_of_x(input):
    if input[0] == "x":
        return 0
    else:
        return 1 + index_of_x(input[1:])

myInput = "abcdefghijklmnopqrstuvwxyz"
print(index_of_x(myInput))
