# Make a function which takes two parameters, sums them up and checks if the sum is divisible by 2. If it is print "Yes it is!" and if not "Nope." (tip: %)

def divByTwo(num1, num2):
    sum = num1 + num2
    if sum % 2 == 0:
        print "Yes it is"
    else:
        print "Nope"

# Testing function
divByTwo(3,6)
