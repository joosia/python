def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Divided by zero!"
    except TypeError:
        return "One or both of your parameters are wrong type!"
    return result

# Testing
print division(5, 0)
print division("a",1)
print division(10,5)
