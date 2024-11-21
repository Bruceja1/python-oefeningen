steps=0
def uniqueLetter(word):
    global steps
    hashMap = {}

    for letter in word:
        if letter in hashMap:
            hashMap[letter] = True
        else:
            hashMap[letter] = False
        steps+=1
    
    for letter in word:
        if hashMap[letter] == False:
            return letter
        steps+=1
        
    return None

word = "minimum"
print(uniqueLetter(word))
print(steps)
