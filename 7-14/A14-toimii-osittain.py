# This assignment might be a bit complicated, but give it a try!
#
# Write a function called symbols that takes a string containing +, = and letters. The function should return True if all of the letters in the string are surrounded by a + symbol. In other words:
#
# print symbols("++++")       # prints: True
# print symbols("====")       # prints: True
# print symbols("+=+=")       # prints: True
# print symbols("++++=++++=") # prints: True
# print symbols("a")          # prints: False, 'a' is not surrounded by + symbols at all!
# print symbols("a+")         # prints: False, 'a' is surrounded by + only on the left side!
# print symbols("+a")         # prints: False, 'a' is surrounded by + only on the right side!
# print symbols("+a+")        # prints: True
# print symbols("+a+====+b+") # prints: True
# print symbols("+a+==x==+b+") # prints: False, 'x' is not surrounded by + symbols at all

def symbols(string):
    chars = []
    letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","i","j","k","l","z","x","c","v","b","n","m"]
    i = 0
    # Convert to list and accept only letters, '+' and '='
    for char in string:
        if char == "=" or char == "+":
            chars.append(char)
        for c in range(len(letters)):
            if char == letters[c]:
                chars.append(char)
    # Loop through string
    for i in range(len(chars)):
        left = False
        letter = False
        right = False
        # Check condition on left side
        if chars[i] == "+":
            left = True
        else:
            left = False
        for j in range(len(letters)):
            # Check middle condition
            if chars[i+1] == letters[j]:
                letter = True
                theLetter = letters[j]
            else:
                letter = False
        # Check condition on right side
        if chars[i+2] == "+" and letter:
            right = True
            break

    # Build result
    if left and letter and right:
        result = "True"
    elif left and letter and right == False:
        result = "False '" + theLetter + "' is surrounded by + only on the left side"
    elif left == False and letter and right:
        result = "False '" + theLetter+ "' is surrounded by + only on the right side"
    elif letter and left == False and right == False:
        result = "False '" + theLetter + "' is not surrounded by + symbols at all"
    else:
        result = " "
    return result

# Testing
testi = "+a++a+a+a+a+a+a+a+a+a+a+a"
print symbols(testi)
