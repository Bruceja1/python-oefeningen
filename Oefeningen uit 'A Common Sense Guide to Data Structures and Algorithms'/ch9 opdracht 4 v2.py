class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def read(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

def reverser(word):
    result = ""
    
    myStack = Stack()

    for letter in word:
        myStack.push(letter)
    print(myStack)

    while True:
        if myStack.isEmpty():
            break
        result += myStack.pop() 
            
    print(result)

myWord = "abcde"
reverser(myWord)
