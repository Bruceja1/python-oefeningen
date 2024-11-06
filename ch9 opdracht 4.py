def reverse_string(s):
    stack = []
    reversed_string = ""

    # push each character of the string onto the stack
    for char in s:
        stack.append(char)

    # pop each character from the stack and append to reversed_string
    while len(stack) != 0:
        reversed_string += stack.pop()

    return reversed_string

myString = "abcde"
print(reverse_string(myString))
