def sumstring(stringlist):
    if len(stringlist) == 1:
        return len(stringlist[0])
    return len(stringlist[0]) + sumstring(stringlist[1:])

myStringlist = ["ab", "c", "def", "ghij"]
print(sumstring(myStringlist))
                    
