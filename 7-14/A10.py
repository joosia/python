# Write a function, called largest, that is given a list of numbers and the function returns the largest number in the list.
#
def largest(numbers):
    maxNum = 0
    for number in numbers:
        if maxNum < number:
            maxNum = number
    return maxNum

#test
print largest([12,23453,123,120,45,3,212,202002,21])
