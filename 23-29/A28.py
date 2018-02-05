import random
theNumber = random.randint(0, 20)
guesses = 1

print "Guess a number between 0 and 20!"

while guesses <= 5:
    userInput = None
    try:
        print "Guess", str(guesses) + "/5: ",
        userInput = int(raw_input())
    except ValueError:
        print "Not a number, try again"
    if userInput == theNumber:
        print "Correct!"
        break
    elif userInput > 20 or userInput < 0:
        print "The guess should be between 0 and 20, try again"
    else:
        print "Sorry, try again!"
        guesses += 1
if guesses > 5:
    print "Game over, you lost! The correct number was", theNumber
