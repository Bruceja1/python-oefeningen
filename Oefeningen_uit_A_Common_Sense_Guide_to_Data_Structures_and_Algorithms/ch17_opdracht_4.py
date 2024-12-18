class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None

        return currentNode

    def insert(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode

                currentNode = newNode

        currentNode.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):
        currentNode = node or self.root
        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)

        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)


    # Eigen Oplossing
    def printAllKeys(self, node=None):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            print(key)
            if childNode:
                self.printAllKeys(childNode)

    # Oplossing Boek
    def traverse(self, node=None):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.traverse(childNode)

    # Eigen Oplossing
    def autocorrect(self, userInput, words=[]):
        string = userInput
        
        if self.search(string):
            print(string)
        
        else:   
            self.autocorrect(string[:-1])

    # Oplossing Boek
    def autocorrect2(self, word):
        currentNode = self.root

        wordFoundSoFar = ""

        for char in word:
            if currentNode.children.get(char):
                wordFoundSoFar += char

                currentNode = currentNode.children.get(char)
            else:
                return wordFoundSoFar + self.collectAllWords(currentNode)[0]

        return word

myTrie = Trie()
myTrie.insert("dog")
myTrie.insert("cat")
myTrie.insert("house")
myTrie.insert("python")
myTrie.insert("computer")

#myTrie.printAllKeys()
#myTrie.traverse()
#print(myTrie.autocorrect("cdfg"))
print(myTrie.autocorrect2("cdfg"))
