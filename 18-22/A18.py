def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Divided by zero!"
    return result

# Testing
print division(5, 0)
print division(10,5)
