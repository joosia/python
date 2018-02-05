def calculator (str, num1, num2):
    result = 0
    if str == "add":
        return num1 + num2
    elif str == "sub":
        return num1 - num2
    elif str == "multiply":
        return num1 * num2
    elif str == "divide":
        try:
            # Python assumes nums are integers if not converted to float
            result = float(num1) / float(num2)
            return float(result)
        except (ZeroDivisionError, TypeError, ValueError):
            return None
    else:
        return None
