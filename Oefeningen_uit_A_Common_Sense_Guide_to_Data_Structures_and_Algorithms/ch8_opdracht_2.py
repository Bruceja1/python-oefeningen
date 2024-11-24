steps = 0

def findDuplicate(array):
    global steps
    hashMap = {}
    for letter in array:
        if letter not in hashMap:
            hashMap[letter] = True
            steps+=1
        else:
            return letter
        steps+=1
    print(hashMap)
       
    return None

myArray = ["a", "b", "c", "d", "c", "e", "f"]
print(findDuplicate(myArray))
print(steps)
