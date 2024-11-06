steps = 0
def missingLetter(sentence):
    global steps
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    hashMap = {}
    
    for letter in sentence:
        hashMap[letter] = True
        steps+=1
    print(hashMap)

    for letter in alphabet:
        if letter not in hashMap:
            return letter
        steps+=1

    return None

sentence = "the quick brown box jumps over a lazy dog"
print(missingLetter(sentence))

print(f"The length of the sentence was {len(sentence)} and took {steps} to complete.")

