import random

# reads the the file line by line and returns a list of words.
def readFile(file):
    f = open(file)
    lines = f.readlines()
    f.close
    return lines

# Get random secret word
def rndWord(file):
    lines = readFile(file);
    numOfWords = len(lines) - 1
    rndNum = random.randint(0, numOfWords)
    theWord = lines[rndNum]
    # Get the length of word and - 1 to remove '\n'
    numOfLetters = len(theWord) - 1
    return theWord

# Line builder
def checker(secretList, chars):
    length = len(secretList)
    line = []
    for i in range(0, length):
        line.append("_")
    matches = 0

    for i in range(0, length):
        for char in chars:
            if char == secretList[i]:
                line[i] = secretList[i]
                matches += 1
        if matches == 0:
            line[i] = "_"
    return line

# Chec if secret word has the char
def charCheck(userInput, chars):
    for char in secretList:
        if userInput == char:
            return True
    return False

# See if the user has won
def validator(userInput):
    user = list(userInput)
    if user == secretList:
        return True
    if line == secretList:
        return True
    return False

secretWord = rndWord("words.txt")
# Convert string to list and remove \n from the end
secretList = list(secretWord)
secretList.pop()
guesses = 5
chars = []
line = []

print "HANGMAN GAME"
while guesses != 0:
    print "Try to guess the word. You have ", guesses, "guesses. Enter a letter"
    userInput = raw_input()
    chars.append(userInput)
    lineCopy = line
    line = checker(secretList, chars)
    print "".join(line)
    if charCheck(userInput, chars) == False:
        guesses -= 1
    if validator(userInput):
        break
if validator(userInput):
    print "Correct, the word was: ", "".join(secretList)
else:
    print "Game Over! The Correct word was: ", "".join(secretList)
