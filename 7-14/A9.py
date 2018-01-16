# Create a function, called "koira", that takes a list of numbers as a parameter and it returns the sum of the numbers in the list. So when given the list [1,2,3,4,5] the function should return 15, list [1,1,1,1] should return 4 etc.

def koira(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Testing
testing = [1,1,1,1,1,1]
print koira(testing)
