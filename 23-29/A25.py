# Add a "divide" operation to your calculator from the previous assignment and make sure it can handle division by zero(use try and except). If a division by zero occurs return None.
#
# What happens when you try to divide 5⁄2? Try to come up with a reason why the result is a bit off.
#
# Note: Returning None like this is usually not the correct choice, but in this case it is done for simplicity.


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
        except ZeroDivisionError:
            return None
    else:
        return None
