# Write a function called sum2 that takes a number and sums all the numbers starting from 0 up to that number.
#
# print sum2(3) # prints: 6
# print sum2(12) # prints: 78

def sum2(num):
    sum = 0
    while num >= 0:
        sum += num
        num -= 1
    return sum

# Testing
print sum2(3)
print sum2(12)
