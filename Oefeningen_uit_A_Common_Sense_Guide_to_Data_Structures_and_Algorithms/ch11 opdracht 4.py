def index_of_x(input, index=-1):
    if input[0] == "x":
        index += 1
        return index

    index += 1
    return index_of_x(input[1:], index)

myInput = "abcdefghijklmnopqrstuvwxyz"
# print(index_of_x(myInput))

# Zonder recursion
def index_of_x_v2(input):
    for i in range(len(input)):
        if input[i] == "x":
            return i

# print(index_of_x_v2(myInput))

# Oplossing boek
def index_of_x_v3(input):
    if input[0] == "x":
        return 0
    return index_of_x_v3(input[1:]) + 1

print(index_of_x_v3(myInput))
