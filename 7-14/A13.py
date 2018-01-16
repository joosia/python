# Write a function vowels that is a given a string and it returns the number of vowels in that string.
# print vowels("aaa") # prints: 3
# print vowels("aba") # prints: 2
# print vowels("bca") # prints: 1

def vowels(string):
    vowels = ["a", "e", "i", "y", "u", "o"]
    counter = 0
    for char in string:
        for vowel in vowels:
            if char == vowel:
                counter += 1
    return counter

#Testing
print vowels("aabsdfbabasbcabascd")
print vowels("iiizxbmcvzxbn")
print vowels("aeiyuo")
