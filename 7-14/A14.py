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
    surrounded = False
    # Convert to list
    for char in string:
        chars.append(char)
    for char in chars:
        if char == "+" || char == "=":
            surrounded = True
        if char
    return surrounded

# Testing
testi = "banaani"
print symbols(testi)
