from typing import *

def calculate(x: Union[str, float], y: Union[str, float], operation: str):
    '''
    This is a function to do basic calculations on two numbers:

    Parameters:
    x: an integer/ a float number
    y: an integer/ a float number
    operation: a string which defines the operation
    '''

    if operation == 'Addition':
        return x + y
    
    elif operation == 'Subtraction':
        if x > y:
            return x - y
        else:
            return x - y

    elif operation == 'Multiplication':
        return x * y

    elif operation == 'Divison':
        return (x / y) if y != 0  else 0