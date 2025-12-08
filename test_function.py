# criteria: refuse all non-integer/float input. multiply input by -1 and return the value. it should take less than 3s to run.
# expected errors: receiving invalid input. in the case of invalid input, return 'invalid input' and end the code.

def inverter(number):
    if isinstance(number, int) or isinstance(number, float) == True:
        newNumber = number * -1
        return newNumber
        print("hi")
    else:
        return "invalid input!"